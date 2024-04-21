from rest_framework import serializers

from webapp.models import Category, Product, Photo, Order, OrderProduct, Cart, StatusOrder

from accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("id", "email", "phone", "first_name", "second_name", "status_active", "role",)
        read_only = ("id",)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")
        read_only = ("id",)


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "category",
            "price",
            "discount",
            "count",
            "size",
            "is_deleted",
            "created_at",
            "updated_at",
        )
        read_only = ("id", "created_at", "updated_at", "is_deleted")


class PhotoSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer(read_only=True)

    class Meta:
        model = Photo
        fields = ("id", "photo", "product_id")
        read_only = ("id",)


class StatusOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusOrder
        fields = ("id", "name")
        read_only = ("id",)


class OrderSerializer(serializers.ModelSerializer):
    users = AccountSerializer(read_only=True)
    status_order = StatusOrderSerializer(read_only=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "users",
            "total_price",
            "address",
            "payment_method",
            "payment_state",
            "delivery_state",
            "status_order"
        )
        read_only = ("id", "total_price", "delivery_state")


class OrderProductSerializer(serializers.ModelSerializer):
    product_pk = ProductSerializer(read_only=True)
    basket_pk = OrderSerializer(read_only=True)

    class Meta:
        model = OrderProduct
        fields = (
            "id",
            "product_pk",
            "price_per_item",
            "basket_pk",
            "count",
        )
        read_only = ("id",)


class CardSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    users = AccountSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = (
            "id",
            "users",
            "product",
            "quantity",
            "created_at",
            "is_deleted",
        )
        read_only = ("id", "is_deleted", "quantity", "created_at")
