# Generated by Django 5.0.6 on 2024-11-20 18:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=20)),
                ('delete_date', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'accesses',
            },
        ),
    ]
