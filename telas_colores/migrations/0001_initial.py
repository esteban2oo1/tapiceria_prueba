# Generated by Django 4.2.7 on 2023-11-10 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('colores', '0003_alter_colores_options'),
        ('tiposTelas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelasColores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colores.colores')),
                ('tela', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiposTelas.tipostelas')),
            ],
        ),
    ]
