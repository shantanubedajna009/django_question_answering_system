# Generated by Django 2.2.3 on 2020-04-07 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qsapp', '0002_auto_20200406_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='atag',
            field=models.UUIDField(unique=True),
        ),
    ]
