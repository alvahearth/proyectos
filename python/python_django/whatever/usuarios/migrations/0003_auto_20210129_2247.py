# Generated by Django 3.1.4 on 2021-01-30 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20210129_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilmodel',
            name='imagen',
            field=models.ImageField(default='default.png', upload_to='profile_pics/'),
        ),
    ]
