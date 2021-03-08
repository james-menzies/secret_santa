# Generated by Django 3.1.6 on 2021-03-08 04:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emoji',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='emojis')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='event_pictures')),
                ('game_length', models.IntegerField(validators=[django.core.validators.MinValueValidator(3), django.core.validators.MaxValueValidator(60)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('activated_at', models.DateTimeField(null=True)),
                ('concluded_at', models.DateTimeField(null=True)),
                ('revealed', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=100, null=True)),
                ('opened', models.BooleanField(default=False)),
            ],
        ),
    ]
