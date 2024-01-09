# Generated by Django 5.0 on 2024-01-09 15:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tp', '0002_alter_site_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='password',
            field=models.CharField(max_length=80, validators=[django.core.validators.MinLengthValidator(8)]),
        ),
    ]
