# Generated by Django 4.0.2 on 2022-04-05 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheca', '0002_histoiry_title_alter_histoiry_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='histoiry',
            name='article',
        ),
        migrations.AddField(
            model_name='histoiry',
            name='articleName',
            field=models.TextField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]