# Generated by Django 3.1.4 on 2021-02-01 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0010_auto_20210131_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moverdinero',
            name='dinero',
            field=models.IntegerField(default=0),
        ),
    ]