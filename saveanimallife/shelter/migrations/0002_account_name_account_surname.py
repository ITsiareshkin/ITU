# Generated by Django 4.1.2 on 2022-11-17 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='name',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='account',
            name='surname',
            field=models.CharField(default='', max_length=15),
        ),
    ]