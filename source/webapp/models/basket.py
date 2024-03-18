from django.db import models
from django.contrib.auth import get_user_model
from enum import Enum


class PaymentMethod(Enum):
    CART = 'КАРТА'
    CASH = 'НАЛИЧНЫЕ'
    QR = 'QR'


class PaymentState(Enum):
    PAID = 'ОПЛАЧЕНО'
    NOT_PAID = 'НЕ ОПЛАЧЕНО'


class Basket(models.Model):
    users = models.ForeignKey(
        to=get_user_model(),
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Цена"
    )
    address = models.CharField(
        max_length=200,
        null=True,
        verbose_name="адрес",
    )
    payment_method = models.CharField(
        max_length=20,
        choices=[(payment.value, payment.name) for payment in PaymentMethod]
    )
    payment_state = models.CharField(
        max_length=20,
        choices=[(payment.value, payment.name) for payment in PaymentState]
    )
    delivery_state = models.BooleanField(
        verbose_name="Статус доставки",
        null=False,
        default=False
    )


class BasketProduct(models.Model):
    product_pk = models.ForeignKey(
        to='webapp.Product',
        related_name='product_pk',
        on_delete=models.CASCADE,
        verbose_name="ID продукта",
        null=True,
        blank=True
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Цена"
    )
    basket_pk = models.ForeignKey(
        to='webapp.Basket',
        related_name='basket_pk',
        on_delete=models.CASCADE,
        verbose_name="ID корзины",
        null=True,
        blank=True
    )

