# Generated by Django 5.0.4 on 2024-05-04 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_categories_rename_initialprice_auctions_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auctions',
            old_name='Price',
            new_name='price',
        ),
    ]