# Generated by Django 4.0.4 on 2022-05-29 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_projetohobby_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='projetohobby',
            name='online',
            field=models.BooleanField(default=False),
        ),
    ]
