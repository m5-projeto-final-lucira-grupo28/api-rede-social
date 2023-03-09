# Generated by Django 4.0.7 on 2023-03-09 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('followers_friendships', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='friendship',
            name='receiving_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiving_friend', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='friendship',
            name='sending_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sending_friend', to=settings.AUTH_USER_MODEL),
        ),
    ]