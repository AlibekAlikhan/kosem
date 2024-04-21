# Generated by Django 5.0.3 on 2024-04-07 16:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_statusorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status_order',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status_order', to='webapp.statusorder', verbose_name='Статус заказа'),
        ),
    ]