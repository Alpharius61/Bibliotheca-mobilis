# Generated by Django 4.0.2 on 2022-03-02 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_charactermodel_pictures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charactermodel',
            name='pictures',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
