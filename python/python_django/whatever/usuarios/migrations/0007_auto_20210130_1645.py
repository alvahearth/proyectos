# Generated by Django 3.1.5 on 2021-01-30 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_auto_20210130_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilmodel',
            name='user',
            field=models.OneToOneField(default=2, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]