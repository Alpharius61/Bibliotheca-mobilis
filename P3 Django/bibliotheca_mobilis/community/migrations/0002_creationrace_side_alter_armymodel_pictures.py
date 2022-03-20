# Generated by Django 4.0.2 on 2022-03-19 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='creationrace',
            name='side',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='community.creationside'),
        ),
        migrations.AlterField(
            model_name='armymodel',
            name='pictures',
            field=models.ImageField(blank=True, null=True, upload_to='community/armypictures'),
        ),
    ]