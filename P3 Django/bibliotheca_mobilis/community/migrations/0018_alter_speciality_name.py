# Generated by Django 4.0.2 on 2022-03-10 22:21

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0017_remove_armymodel_speciality_armymodel_speciality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciality',
            name='name',
            field=multiselectfield.db.fields.MultiSelectField(max_length=200),
        ),
    ]
