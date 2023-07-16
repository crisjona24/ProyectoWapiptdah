# Generated by Django 4.2.2 on 2023-06-24 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APPWapiptdah', '0007_curso_usuario_comun'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='grado_tdah_f',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categorias', to='APPWapiptdah.gradotdah'),
        ),
        migrations.AddField(
            model_name='categoria',
            name='slug_categoria',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
