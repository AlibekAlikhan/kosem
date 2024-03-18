from rest_framework import serializers

from webapp.models import Category, Product, Photo


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
            "updated_at"
        )
        read_only = ("id", "created_at", "updated_at", "is_deleted")


class PhotoSerializer(serializers.ModelSerializer):
    product_id = CategorySerializer(read_only=True)
    class Meta:
        model = Photo
        fields = ("id", "photo", "product_id")
        read_only = ("id",)
