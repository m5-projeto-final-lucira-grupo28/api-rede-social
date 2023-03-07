# Generated by Django 4.1.7 on 2023-03-07 18:39

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField(max_length=500)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("private", models.BooleanField(default=False)),
                ("can_comment", models.BooleanField(default=True)),
            ],
            options={
                "ordering": ("id",),
            },
        ),
    ]
