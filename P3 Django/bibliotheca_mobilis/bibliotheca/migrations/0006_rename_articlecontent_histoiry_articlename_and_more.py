# Generated by Django 4.0.2 on 2022-04-05 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheca', '0005_rename_title_histoiry_articletitle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='histoiry',
            old_name='articleContent',
            new_name='articleName',
        ),
        migrations.RenameField(
            model_name='histoiry',
            old_name='articletitle',
            new_name='title',
        ),
    ]
