# Generated by Django 4.0.4 on 2022-05-29 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_comentario_laboratorio_tecnologia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tecnologia',
            name='data',
        ),
    ]
