# Generated by Django 4.0.2 on 2022-03-07 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0007_alter_charactersmodel_chaosaspect_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charactersmodel',
            name='pictures',
            field=models.ImageField(blank=True, null=True, upload_to='community\\characterspictures'),
        ),
    ]