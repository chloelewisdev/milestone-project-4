# Generated by Django 3.2.1 on 2021-05-23 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
    ]
