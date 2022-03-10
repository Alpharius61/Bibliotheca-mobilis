# Generated by Django 4.0.2 on 2022-03-10 22:48

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0018_alter_speciality_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='specialities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('speciality', multiselectfield.db.fields.MultiSelectField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='speciality',
        ),
        migrations.AlterField(
            model_name='armymodel',
            name='speciality',
            field=models.ManyToManyField(to='community.specialities'),
        ),
        migrations.AlterField(
            model_name='charactersmodel',
            name='speciality',
            field=models.ManyToManyField(to='community.specialities'),
        ),
    ]
