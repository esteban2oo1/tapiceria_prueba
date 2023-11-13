# Generated by Django 4.2.7 on 2023-11-10 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tiposMateriales', '0001_initial'),
        ('tiposProductos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=45, null=True)),
                ('fecha_fabricacion', models.DateField(null=True)),
                ('precio_costo', models.IntegerField()),
                ('precio_venta', models.IntegerField()),
                ('tipoMaterial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiposMateriales.tiposmateriales')),
                ('tipoProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiposProductos.tiposproductos')),
            ],
        ),
    ]