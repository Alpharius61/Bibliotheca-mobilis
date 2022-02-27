# Generated by Django 4.0.2 on 2022-02-26 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_remove_userorigin_name_userorigin_origin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userorigin',
            name='origin',
        ),
        migrations.AddField(
            model_name='userorigin',
            name='name',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
