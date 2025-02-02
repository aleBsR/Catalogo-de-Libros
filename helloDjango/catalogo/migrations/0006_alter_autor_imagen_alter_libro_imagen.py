# Generated by Django 5.0.1 on 2024-02-07 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0005_libro_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/autor'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/libro'),
        ),
    ]
