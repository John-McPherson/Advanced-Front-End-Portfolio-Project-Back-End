# Generated by Django 3.2.15 on 2022-08-27 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="colorist",
            field=models.BooleanField(default=False),
        ),
    ]
