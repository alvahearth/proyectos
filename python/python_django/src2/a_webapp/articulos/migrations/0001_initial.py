# Generated by Django 3.1.5 on 2021-01-22 16:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, unique=True, verbose_name='Titulo')),
                ('contenido', models.TextField()),
                ('fecha_publicado', models.DateTimeField(default=datetime.datetime(2021, 1, 22, 16, 59, 43, 83885, tzinfo=utc))),
            ],
        ),
    ]
