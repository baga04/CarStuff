# Generated by Django 5.2.1 on 2025-05-21 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]
