# Generated by Django 5.0.3 on 2024-03-22 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_remove_basketproduct_price_basketproduct_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='basketproduct',
            name='price_per_item',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена из продукта'),
        ),
        migrations.AlterField(
            model_name='basketproduct',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='общая цена'),
        ),
    ]