# Generated by Django 3.2.15 on 2022-09-24 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0003_alter_page_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="page",
            options={"ordering": ["title"]},
        ),
    ]
