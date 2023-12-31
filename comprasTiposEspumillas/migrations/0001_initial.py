# Generated by Django 4.2.7 on 2023-11-11 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tiposEspumillas', '0001_initial'),
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComprasTiposEspumillas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.compras')),
                ('tipoEspumilla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiposEspumillas.tiposespumillas')),
            ],
        ),
    ]
