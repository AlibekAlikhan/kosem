from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Название категории",
    )

    def __str__(self):
        return f"{self.name}"
