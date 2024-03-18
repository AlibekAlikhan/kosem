from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.generics import GenericAPIView
from api.serializers import ProductSerializer

from webapp.models import Product, Category


class ProductSimpleView(GenericAPIView):
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        try:
            events = Product.objects.all()
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        else:
            serializer = ProductSerializer(events, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        try:
            data['category'] = Category.objects.get(id=data.get('category'))
            Product.objects.create(**data)
            return Response({"create": "успешно создано"})
        except Exception:
            response = Response({'errors': "ошибка"})
            response.status_code = 400
            return response


class ProductApiView(GenericAPIView):
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        try:
            objects = get_object_or_404(Product, pk=kwargs.get("pk"))
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        serializer = ProductSerializer(objects)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        data = json.loads(request.body)
        objects = get_object_or_404(Product, pk=kwargs.get("pk"))
        serializer = ProductSerializer(objects, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            response = Response({'errors': serializer.errors})
            response.status_code = 400
            return response

    def delete(self, request, *args, **kwargs):
        try:
            objects = get_object_or_404(Product, pk=kwargs.get("pk"))
            objects.delete()
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        return Response({f"delte - {kwargs.get('pk')}": "мягкое удаление успешно выполнелось"})
