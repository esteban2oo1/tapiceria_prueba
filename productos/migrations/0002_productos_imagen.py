# Generated by Django 4.2.7 on 2023-11-14 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(null=True, upload_to='producto'),
        ),
    ]
