from django.contrib.auth import get_user_model
from django.db import models


class Gallery(models.Model):
    author = models.ForeignKey(
        verbose_name="Автор",
        to=get_user_model(),
        related_name="cv",
        on_delete=models.CASCADE,
    )
    photo = models.ImageField(
        null=True,
        blank=True,
        upload_to="user_pic",
        verbose_name="Фото",
        default="user_pic/default_user_pic.jpeg",
    )
    signature = models.TextField(
        max_length=100,
        verbose_name="Уровень образования",
        blank=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания",
    )
    favorites = models.ManyToManyField(
        verbose_name='Подписки',
        to='accounts.Account',
        related_name='favorites')