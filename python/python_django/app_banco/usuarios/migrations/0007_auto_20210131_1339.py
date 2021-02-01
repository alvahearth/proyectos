# Generated by Django 3.1.4 on 2021-01-31 16:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_auto_20210131_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Última conexión'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Última conexión'),
        ),
    ]
