# Generated by Django 4.1.2 on 2022-11-25 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_products_image10_products_image3_products_image4_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='image10',
        ),
    ]