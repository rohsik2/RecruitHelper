# Generated by Django 2.2.4 on 2020-09-30 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created_date',
            new_name='published_date',
        ),
    ]
