# Generated by Django 3.1.5 on 2021-01-22 17:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='fecha_publicado',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 22, 17, 34, 7, 823989, tzinfo=utc)),
        ),
    ]
