# Generated by Django 4.0.2 on 2022-04-05 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheca', '0003_remove_histoiry_article_histoiry_articlename'),
    ]

    operations = [
        migrations.RenameField(
            model_name='histoiry',
            old_name='articleName',
            new_name='articleContent',
        ),
    ]
