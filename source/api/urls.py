from django.urls import path

from api.views import favorites_api

urlpatterns = [
    path('favorites/<int:pk>', favorites_api, name='favorites'),
]