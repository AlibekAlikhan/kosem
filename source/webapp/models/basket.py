from django.db import models
from django.contrib.auth import get_user_model
from enum import Enum
from django.utils import timezone


class PaymentMethod(Enum):
    CART = 'КАРТА'
    CASH = 'НАЛИЧНЫЕ'
    QR = 'QR'


class PaymentState(Enum):
    PAID = 'ОПЛАЧЕНО'
    NOT_PAID = 'НЕ ОПЛАЧЕНО'


class StatusOrder(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Название статуса",
    )

    def __str__(self):
        return f"{self.name}"


class Cart(models.Model):
    users = models.ForeignKey(
        to=get_user_model(),
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    product = models.ForeignKey(
        to='webapp.Product',
        related_name='product_id',
        on_delete=models.CASCADE,
        verbose_name="ID продукта",
        null=True,
        blank=True
    )
    quantity = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Количество'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления'
    )
    is_deleted = models.BooleanField(
        verbose_name="Удалено",
        null=False,
        default=False
    )

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()


class Order(models.Model):
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
    is_deleted = models.BooleanField(
        verbose_name="Удалено",
        null=False,
        default=False
    )
    status_order = models.ForeignKey(
        to='webapp.StatusOrder',
        related_name='status_order',
        on_delete=models.CASCADE,
        verbose_name="Статус заказа",
        null=True,
        blank=True,
        default=1
    )

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()


class OrderProduct(models.Model):
    product_pk = models.ForeignKey(
        to='webapp.Product',
        related_name='product_pk',
        on_delete=models.CASCADE,
        verbose_name="ID продукта",
        null=True,
        blank=True
    )
    price_per_item = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Цена из продукта"
    )
    basket_pk = models.ForeignKey(
        to='webapp.Order',
        related_name='basket_pk',
        on_delete=models.CASCADE,
        verbose_name="ID корзины",
        null=True,
        blank=True
    )
    count = models.IntegerField(
        default=1
    )
    is_deleted = models.BooleanField(
        verbose_name="Удалено",
        null=False,
        default=False
    )

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    # def save(self, *args, **kwargs):
    #     price_per_item = self.product_pk.price
    #     self.price_per_item = price_per_item
    #     self.total_price = int(self.count) * price_per_item
    #     super(OrderProduct, self).save(*args, **kwargs)

    def sum_total_price(self, using=None, keep_parents=False):
        price_per_item = self.product_pk.price
        self.price_per_item = price_per_item
        self.total_price = int(self.count) * price_per_item
        self.save()
