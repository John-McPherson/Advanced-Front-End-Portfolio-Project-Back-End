# Generated by Django 3.2.15 on 2022-08-21 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('color', models.BooleanField(default=False)),
                ('pages', models.IntegerField(default=22)),
                ('artists', models.ManyToManyField(related_name='artists', related_query_name='artists', to='profiles.Profile')),
                ('editors', models.ManyToManyField(related_name='editors', related_query_name='editors', to='profiles.Profile')),
                ('letterers', models.ManyToManyField(related_name='letterers', related_query_name='letterers', to='profiles.Profile')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('writers', models.ManyToManyField(related_name='writers', related_query_name='writers', to='profiles.Profile')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]