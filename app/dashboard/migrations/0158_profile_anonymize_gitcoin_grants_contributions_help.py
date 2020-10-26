# Generated by Django 2.2.4 on 2020-10-26 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0157_auto_20201016_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='anonymize_gitcoin_grants_contributions_help',
            field=models.BooleanField(default=False, help_text='If this option is chosen, we will anonymize your Gitcoin Grants contributions'),
        ),
    ]
