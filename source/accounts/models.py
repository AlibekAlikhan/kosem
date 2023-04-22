from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import UserManager


class Account(AbstractUser):
    email = models.EmailField(
        verbose_name="Электронная почта", unique=True, blank=False
    )
    phone = models.CharField(verbose_name="Номер телефона", blank=True, max_length=30)
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to="user_pic",
        verbose_name="Аватар",
        default="user_pic/default_user_pic.jpeg",
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    object = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
