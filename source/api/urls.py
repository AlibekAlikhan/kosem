from django.urls import path
from api.views.category_api import CategoryApiView, CategorySimpleView
from api.views.product_api import ProductSimpleView, ProductApiView
from api.views.card import CardSimpleView, CardApiView
from api.views.order import OrderSimpleView, OrderAllGetView, OrderDetailApiView
from api.views.order_admin import OrderAllAdminGetView, OrderDetailAdminApiView, StatusOrderSimpleView, \
    StatusOrderApiView

urlpatterns = [
    path('category/', CategorySimpleView.as_view(), name="category_list"),
    path('category/<int:pk>', CategoryApiView.as_view(), name="category"),
    path('product/', ProductSimpleView.as_view(), name="product_list"),
    path('product/<int:pk>', ProductApiView.as_view(), name="product"),
    path('cart/', CardSimpleView.as_view(), name="cart_list"),
    path('cart/<int:pk>', CardApiView.as_view(), name="cart"),
    path('order/post', OrderSimpleView.as_view(), name="order_list"),
    path('orders/<int:pk>', OrderAllGetView.as_view(), name="order_user_list"),
    path('orders/detail/<int:pk>', OrderDetailApiView.as_view(), name="order"),
    path('orders/admin/', OrderAllAdminGetView.as_view(), name="order_admin_list"),
    path('orders/admin/<int:pk>', OrderDetailAdminApiView.as_view(), name="order_admin"),
    path('status/orders/admin/', StatusOrderSimpleView.as_view(), name="order_status_list"),
    path('status/orders/admin/<int:pk>', StatusOrderApiView.as_view(), name="order_status"),
]
