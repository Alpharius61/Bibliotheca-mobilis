# Generated by Django 4.0.2 on 2022-04-05 20:07

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheca', '0009_rename_histoiry_history_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='parents',
        ),
        migrations.AddField(
            model_name='history',
            name='level',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='history',
            name='lft',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='history',
            name='name',
            field=models.CharField(default=0, max_length=32, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='history',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='bibliotheca.history'),
        ),
        migrations.AddField(
            model_name='history',
            name='rght',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='history',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
            preserve_default=False,
        ),
    ]
