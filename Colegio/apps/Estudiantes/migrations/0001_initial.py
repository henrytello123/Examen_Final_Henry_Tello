# Generated by Django 4.1 on 2022-08-31 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colegio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=40)),
                ('Edad', models.IntegerField()),
                ('Grado', models.CharField(max_length=15)),
                ('Procedencia', models.CharField(max_length=40)),
            ],
        ),
    ]
