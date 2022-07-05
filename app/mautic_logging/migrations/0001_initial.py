# Generated by Django 2.2.24 on 2022-07-05 06:10

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import economy.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MauticLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('status_code', models.IntegerField()),
                ('method', models.CharField(max_length=5)),
                ('endpoint', models.TextField()),
                ('payload', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('params', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
