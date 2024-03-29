from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.generics import GenericAPIView

from api.serializers import CategorySerializer

from webapp.models import Category


class CategorySimpleView(GenericAPIView):
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        try:
            events = Category.objects.all()
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        else:
            serializer = CategorySerializer(events, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        try:
            Category.objects.create(**data)
            return Response({"create": "успешно создано"})
        except Exception:
            response = Response({'errors': "ошибка"})
            response.status_code = 400
            return response


class CategoryApiView(GenericAPIView):
    serializer_class = CategorySerializer

    def delete(self, request, *args, **kwargs):
        try:
            objects = get_object_or_404(Category, pk=kwargs.get("pk"))
            objects.delete()
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        return Response({f"delte - {kwargs.get('pk')}": "мягкое удаление успешно выполнелось"})
