# Generated by Django 4.0.4 on 2022-05-29 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projetohobby',
            name='data',
            field=models.DateTimeField(),
        ),
    ]