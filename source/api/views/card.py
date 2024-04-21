from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.generics import GenericAPIView
from api.serializers import CardSerializer
from webapp.models import Product, Cart
from accounts.models import Account


class CardSimpleView(GenericAPIView):
    serializer_class = CardSerializer

    def get(self, request, *args, **kwargs):
        try:
            card = Cart.objects.all()
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        else:
            serializer = CardSerializer(card, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        try:
            product = Product.objects.get(id=data.get('product'))
            users = Account.objects.get(id=data.get('users'))
            carts = Cart.objects.filter(users=users, product=product, is_deleted=False)
            if carts.exists():
                cart = carts.first()
                if cart:
                    cart.quantity += 1
                    cart.save()
                    return Response({"create": "успешно добавлен"})
            else:
                Cart.objects.create(users=users, product=product, quantity=1)
                return Response({"create": "успешно создано"})

        except Exception:
            response = Response({'errors': "ошибка"})
            response.status_code = 400
            return response


class CardApiView(GenericAPIView):
    serializer_class = CardSerializer

    def get(self, request, *args, **kwargs):
        try:
            objects = get_object_or_404(Account, pk=kwargs.get("pk"))
            cart = Cart.objects.filter(users=objects, is_deleted=False)
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        serializer = CardSerializer(cart, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        data = json.loads(request.body)
        objects = get_object_or_404(Cart, pk=kwargs.get("pk"))
        serializer = CardSerializer(objects, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            response = Response({'errors': serializer.errors})
            response.status_code = 400
            return response

    def delete(self, request, *args, **kwargs):
        try:
            objects = get_object_or_404(Cart, pk=kwargs.get("pk"))
            objects.delete()
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        return Response({f"delte - {kwargs.get('pk')}": "мягкое удаление успешно выполнелось"})
