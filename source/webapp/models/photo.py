from django.db import models
from django.core.validators import validate_image_file_extension


class Photo(models.Model):
    photo = models.ImageField(
        null=False,
        blank=False,
        upload_to="user_pic",
        verbose_name="Фото",
        validators=[validate_image_file_extension]
    )
    product_id = models.ForeignKey(
        to='webapp.Product',
        related_name='product_photo',
        on_delete=models.CASCADE,
        verbose_name="Фото товара",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.photo}"
