# Generated by Django 5.0.3 on 2024-03-10 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_data_alter_product_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='data',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
