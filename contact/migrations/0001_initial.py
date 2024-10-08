# Generated by Django 5.0 on 2024-10-04 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2024, 10, 4, 17, 36, 12, 280641, tzinfo=datetime.timezone.utc))),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
