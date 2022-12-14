# Generated by Django 3.2.13 on 2022-12-13 06:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermodel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='follows',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]