from django.db import models
from enum import Enum


class ProductSize(Enum):
    M = 'M'
    S = 'S'
    XL = 'XL'
    XSS = 'XSS'


class Product(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Название продукта",
    )
    description = models.TextField(
        max_length=3000,
        null=False,
        verbose_name="Описание",
    )
    category = models.ForeignKey(
        to='webapp.Category',
        related_name='category',
        on_delete=models.CASCADE,
        verbose_name="Категория",
        null=True,
        blank=True
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Цена"
    )
    discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Скидка"
    )
    count = models.IntegerField(
        null=False,
        blank=False,
        verbose_name="количество"
    )
    size = models.CharField(
        max_length=20,
        choices=[(product_size.value, product_size.name) for product_size in ProductSize]
    )
    is_deleted = models.BooleanField(
        verbose_name="Удалено",
        null=False,
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата добавления"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обнавления"
    )
