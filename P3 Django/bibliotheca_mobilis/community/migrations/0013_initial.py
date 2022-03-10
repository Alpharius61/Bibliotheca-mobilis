# Generated by Django 4.0.2 on 2022-03-09 12:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0004_alter_creationrace_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0012_remove_charactersmodel_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='charactersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('biography', models.TextField(max_length=10000)),
                ('pictures', models.ImageField(blank=True, null=True, upload_to='community\\characterspictures')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('chaosAspect', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.chaosaspectvenerated')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.creationrace')),
                ('side', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.creationside')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.creationtype')),
            ],
        ),
        migrations.CreateModel(
            name='armyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('history', models.TextField(max_length=200)),
                ('pictures', models.ImageField(blank=True, null=True, upload_to='community\\characterspictures')),
                ('actualChef', models.CharField(max_length=50)),
                ('firstChef', models.CharField(blank=True, max_length=50, null=True)),
                ('speciality', models.CharField(max_length=100, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('chaosAspect', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.chaosaspectvenerated')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.creationrace')),
                ('side', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.creationside')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.creationtype')),
            ],
        ),
    ]