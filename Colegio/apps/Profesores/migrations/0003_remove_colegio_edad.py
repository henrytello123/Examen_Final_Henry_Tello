# Generated by Django 4.1 on 2022-08-31 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profesores', '0002_colegio_edad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colegio',
            name='Edad',
        ),
    ]
