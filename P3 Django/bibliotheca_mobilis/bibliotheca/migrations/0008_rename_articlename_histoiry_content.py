# Generated by Django 4.0.2 on 2022-04-05 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheca', '0007_alter_histoiry_parents'),
    ]

    operations = [
        migrations.RenameField(
            model_name='histoiry',
            old_name='articleName',
            new_name='content',
        ),
    ]
