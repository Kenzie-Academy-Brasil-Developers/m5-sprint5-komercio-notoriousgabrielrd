# Generated by Django 4.0.6 on 2022-07-08 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productsmodel',
            old_name='user',
            new_name='seller',
        ),
    ]