# Generated by Django 4.2.7 on 2023-11-27 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='creator',
        ),
    ]
