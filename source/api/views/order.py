from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.generics import GenericAPIView
from api.serializers import OrderSerializer, OrderProductSerializer
from webapp.models import Order, Cart, OrderProduct
from django.forms import ValidationError
from accounts.models import Account


class OrderSimpleView(GenericAPIView):
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        try:
            users = Account.objects.get(id=data.get('users'))
            cart_items = Cart.objects.filter(users=users, is_deleted=False)
            if cart_items.exists():
                data['users'] = Account.objects.get(id=data.get('users'))
                data_price_total = 0
                for cart_item in cart_items:
                    data_price_total += cart_item.product.price * cart_item.quantity
                data['total_price'] = data_price_total
                order = Order.objects.create(**data)

                for cart_item in cart_items:
                    product_pk = cart_item.product
                    price_per_item = cart_item.product.price
                    count = cart_item.quantity
                    if product_pk.count < count:
                        raise ValidationError('Недостаточное количество товара')
                    OrderProduct.objects.create(
                        product_pk=product_pk,
                        price_per_item=price_per_item,
                        basket_pk=order,
                        count=count,
                    )
                    product_pk.count -= count
                    product_pk.save()
                    cart_item.delete()
            return Response({"create": "успешно создано"})

        except Exception:
            response = Response({'errors': "ошибка"})
            response.status_code = 400
            return response


class OrderAllGetView(GenericAPIView):
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        try:
            objects = get_object_or_404(Account, pk=kwargs.get("pk"))
            events = Order.objects.filter(users=objects, is_deleted=False)
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        else:
            serializer = OrderSerializer(events, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class OrderDetailApiView(GenericAPIView):
    serializer_class = OrderProductSerializer

    def get(self, request, *args, **kwargs):
        try:
            objects = get_object_or_404(Order, pk=kwargs.get("pk"))
            order = OrderProduct.objects.filter(basket_pk=objects, is_deleted=False)
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        serializer = OrderProductSerializer(order, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        try:
            objects = get_object_or_404(Order, pk=kwargs.get("pk"))
            order = OrderProduct.objects.filter(basket_pk=objects)
            objects.delete()
            for i in order:
                i.delete()
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        return Response({f"delte - {kwargs.get('pk')}": "мягкое удаление успешно выполнелось"})
