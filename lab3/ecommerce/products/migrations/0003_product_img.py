# Generated by Django 5.0.1 on 2024-02-04 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_products_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
