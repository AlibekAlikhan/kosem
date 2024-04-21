from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.generics import GenericAPIView
from api.serializers import OrderSerializer, OrderProductSerializer, StatusOrderSerializer
from webapp.models import Order, Cart, OrderProduct, StatusOrder


class OrderAllAdminGetView(GenericAPIView):
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        try:
            events = Order.objects.all()
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        else:
            serializer = OrderSerializer(events, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class OrderDetailAdminApiView(GenericAPIView):
    serializer_class = OrderProductSerializer

    def get(self, request, *args, **kwargs):
        try:
            objects = get_object_or_404(Order, pk=kwargs.get("pk"))
            order = OrderProduct.objects.filter(basket_pk=objects)
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

    def put(self, request, *args, **kwargs):
        data = json.loads(request.body)
        objects = get_object_or_404(Order, pk=kwargs.get("pk"))
        serializer = OrderSerializer(objects, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            response = Response({'errors': serializer.errors})
            response.status_code = 400
            return response


class StatusOrderSimpleView(GenericAPIView):
    serializer_class = StatusOrderSerializer

    def get(self, request, *args, **kwargs):
        try:
            events = StatusOrder.objects.all()
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        else:
            serializer = StatusOrderSerializer(events, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        try:
            StatusOrder.objects.create(**data)
            return Response({"create": "успешно создано"})
        except Exception:
            response = Response({'errors': "ошибка"})
            response.status_code = 400
            return response


class StatusOrderApiView(GenericAPIView):
    serializer_class = StatusOrderSerializer

    def delete(self, request, *args, **kwargs):
        try:
            objects = get_object_or_404(StatusOrder, pk=kwargs.get("pk"))
            objects.delete()
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        return Response({f"delte - {kwargs.get('pk')}": "мягкое удаление успешно выполнелось"})