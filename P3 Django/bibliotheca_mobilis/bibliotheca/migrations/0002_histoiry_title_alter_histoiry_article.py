# Generated by Django 4.0.2 on 2022-03-09 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheca', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='histoiry',
            name='title',
            field=models.CharField(default=None, max_length=70),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='histoiry',
            name='article',
            field=models.TextField(max_length=20000),
        ),
    ]
