from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import UserManager


class Account(AbstractUser):
    email = models.EmailField(
        verbose_name="Электронная почта",
        unique=True,
        blank=False
    )
    username = models.CharField(
        verbose_name="имя пользователя",
        blank=True,
        max_length=30
    )
    phone = models.CharField(
        verbose_name="Номер телефона",
        blank=True,
        max_length=30
    )
    first_name = models.CharField(
        verbose_name="Имя",
        blank=True,
        max_length=30
    )
    second_name = models.CharField(
        verbose_name="Фамилия",
        blank=True,
        max_length=30
    )
    status_active = models.BooleanField(
        verbose_name="Статус активности",
        null=False,
        default=True
    )
    role = models.ForeignKey(
        to='accounts.Role',
        related_name='role_for_account',
        on_delete=models.SET_NULL,
        verbose_name="Роль",
        null=True,
        blank=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    object = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
