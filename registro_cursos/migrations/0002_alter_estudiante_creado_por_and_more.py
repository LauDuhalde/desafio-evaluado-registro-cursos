# Generated by Django 4.2 on 2024-05-01 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_cursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='creado_por',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='creado_por',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
