# Generated by Django 4.0.6 on 2022-07-12 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsmodel',
            old_name='age',
            new_name='full_description',
        ),
        migrations.RenameField(
            model_name='newsmodel',
            old_name='sex',
            new_name='short_description',
        ),
    ]
