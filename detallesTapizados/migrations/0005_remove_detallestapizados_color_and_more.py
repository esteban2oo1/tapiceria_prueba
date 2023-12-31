# Generated by Django 4.2.4 on 2023-12-15 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('telas_colores', '0001_initial'),
        ('tiposMateriales', '0001_initial'),
        ('detallesTapizados', '0004_detallestapizados_cantidad_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallestapizados',
            name='color',
        ),
        migrations.RemoveField(
            model_name='detallestapizados',
            name='tipoTela',
        ),
        migrations.AddField(
            model_name='detallestapizados',
            name='telaColor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='telas_colores.telascolores'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detallestapizados',
            name='tipoMaterial',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tiposMateriales.tiposmateriales'),
            preserve_default=False,
        ),
    ]
