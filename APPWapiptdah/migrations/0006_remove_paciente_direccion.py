# Generated by Django 4.2.2 on 2023-06-22 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APPWapiptdah', '0005_remove_paciente_antecedente_medico_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='direccion',
        ),
    ]
