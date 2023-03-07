# Generated by Django 4.1.7 on 2023-03-07 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("posts", "0001_initial"),
        ("comments", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="posts.post",
            ),
        ),
    ]
