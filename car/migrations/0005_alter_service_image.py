# Generated by Django 4.2.5 on 2023-09-19 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_contact_accept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='image'),
        ),
    ]
