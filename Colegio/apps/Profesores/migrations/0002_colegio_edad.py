# Generated by Django 4.1 on 2022-08-31 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profesores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='colegio',
            name='Edad',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
