# Generated by Django 4.2.5 on 2023-11-06 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order_coupon_order_total_with_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart_coupon', to='orders.coupon'),
        ),
        migrations.AddField(
            model_name='cart',
            name='total_with_coupon',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
