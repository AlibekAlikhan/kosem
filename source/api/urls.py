from django.urls import path

from api.views.category_api import CategoryApiView, CategorySimpleView
from api.views.product_api import ProductSimpleView, ProductApiView

urlpatterns = [
    path('category/', CategorySimpleView.as_view(), name="category_list"),
    path('category/<int:pk>', CategoryApiView.as_view(), name="category"),
    path('product/', ProductSimpleView.as_view(), name="product_list"),
    path('product/<int:pk>', ProductApiView.as_view(), name="product"),
]
