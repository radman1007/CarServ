# Generated by Django 4.2.5 on 2023-09-21 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0005_alter_service_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='image',
        ),
    ]
