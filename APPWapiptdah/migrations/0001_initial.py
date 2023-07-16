# Generated by Django 4.2.1 on 2023-06-02 02:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=140)),
                ('apellido', models.CharField(max_length=140)),
                ('correo_electronico', models.EmailField(blank=True, max_length=254, unique=True)),
                ('numero_celular', models.CharField(max_length=10, null=True)),
                ('dni', models.CharField(max_length=10, unique=True)),
                ('direccion', models.CharField(max_length=140)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=16, validators=[django.core.validators.MinLengthValidator(8)])),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
    ]
