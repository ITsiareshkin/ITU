# Generated by Django 4.1.2 on 2022-11-20 20:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0002_alter_animal_options_alter_animal_photo_walk'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='walk',
            options={'ordering': ('-starting',)},
        ),
        migrations.AlterField(
            model_name='walk',
            name='walker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
