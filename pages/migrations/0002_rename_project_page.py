# Generated by Django 3.2.15 on 2022-08-27 13:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("project", "0002_auto_20220827_1351"),
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Project",
            new_name="Page",
        ),
    ]
