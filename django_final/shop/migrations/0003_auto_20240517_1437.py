# Generated by Django 3.2.16 on 2024-05-17 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='email',
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.seller'),
        ),
    ]
