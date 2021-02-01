# Generated by Django 3.1.4 on 2021-02-01 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_dinero'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoverDinero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dinero', models.IntegerField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usuarios.dinero')),
            ],
        ),
    ]
