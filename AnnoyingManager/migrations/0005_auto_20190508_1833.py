# Generated by Django 2.1.4 on 2019-05-08 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnnoyingManager', '0004_auto_20190508_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.IntegerField(blank=True, default=1557340416),
        ),
    ]