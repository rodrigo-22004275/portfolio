# Generated by Django 4.0.4 on 2022-06-15 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_tfc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tfc',
            name='video',
            field=models.CharField(max_length=100),
        ),
    ]
