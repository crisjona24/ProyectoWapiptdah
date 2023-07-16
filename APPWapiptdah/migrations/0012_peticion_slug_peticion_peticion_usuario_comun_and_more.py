# Generated by Django 4.2.2 on 2023-07-02 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APPWapiptdah', '0011_contenido_categoria_contenido_slug_contenido'),
    ]

    operations = [
        migrations.AddField(
            model_name='peticion',
            name='slug_peticion',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='peticion',
            name='usuario_comun',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='peticiones', to='APPWapiptdah.usuariocomun'),
        ),
        migrations.AddField(
            model_name='reportes',
            name='contenido_f',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reportes_contenido', to='APPWapiptdah.contenido'),
        ),
        migrations.AddField(
            model_name='reportes',
            name='slug_reporte',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='reportes',
            name='usuario_comun',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reportes', to='APPWapiptdah.usuariocomun'),
        ),
        migrations.AddField(
            model_name='resultados',
            name='contenido',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resultados_c', to='APPWapiptdah.contenido'),
        ),
        migrations.AddField(
            model_name='resultados',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resultados', to='APPWapiptdah.paciente'),
        ),
        migrations.AddField(
            model_name='resultados',
            name='slug_resultado',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='sala',
            name='slug_sala',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='sala',
            name='usuario_comun',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='salas', to='APPWapiptdah.usuariocomun'),
        ),
    ]
