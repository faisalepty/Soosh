# Generated by Django 4.2.5 on 2023-11-03 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_category_remove_product_brand_remove_product_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='elctronics_subcat',
            field=models.CharField(blank=True, choices=[('Apple', 'Apple'), ('Sumsung', 'Sumsung'), ('Playstation', 'Playstation')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='snicker_subcat',
            field=models.CharField(blank=True, choices=[('Nike', 'Nike'), ('Jordan', 'Jordan'), ('Adidas', 'Adidas')], max_length=50, null=True),
        ),
    ]
