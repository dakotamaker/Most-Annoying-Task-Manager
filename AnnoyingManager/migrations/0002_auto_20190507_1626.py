# Generated by Django 2.1.3 on 2019-05-07 16:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnnoyingManager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersettings',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='email_frequency',
            field=models.FloatField(default=10, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='user',
            name='text_frequency',
            field=models.FloatField(default=10, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.IntegerField(blank=True, default=1557246365),
        ),
        migrations.DeleteModel(
            name='UserSettings',
        ),
    ]
