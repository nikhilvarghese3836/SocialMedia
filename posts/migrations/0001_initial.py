# Generated by Django 3.2.13 on 2022-12-13 06:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('post_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('text', models.TextField()),
                ('media_url', models.CharField(blank=True, max_length=250)),
                ('post_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
