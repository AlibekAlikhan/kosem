# Generated by Django 5.0.3 on 2024-04-08 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_order_status_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(help_text='полное описание продукта', max_length=3000, verbose_name='Описание'),
        ),
    ]
