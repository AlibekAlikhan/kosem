from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.generics import GenericAPIView
from api.serializers import PhotoSerializer
from webapp.models import Photo, Product


class PhotoSimpleView(GenericAPIView):
    serializer_class = PhotoSerializer

    def get(self, request, *args, **kwargs):
        try:
            events = Photo.objects.all()
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        else:
            serializer = PhotoSerializer(events, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        try:
            data['product_id'] = Product.objects.get(id=data.get('product_id'))
            Photo.objects.create(**data)
            return Response({"create": "успешно создано"})
        except Exception:
            response = Response({'errors': "ошибка"})
            response.status_code = 400
            return response


class PhotoApiView(GenericAPIView):
    serializer_class = PhotoSerializer

    def delete(self, request, *args, **kwargs):
        try:
            objects = get_object_or_404(Photo, pk=kwargs.get("pk"))
            objects.delete()
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        return Response({f"delte - {kwargs.get('pk')}": "мягкое удаление успешно выполнелось"})
