# Generated by Django 2.2.3 on 2020-04-07 16:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('qsapp', '0004_auto_20200407_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='atag',
            field=models.UUIDField(default=uuid.UUID('35523311-e296-4394-a5ea-b550ea3dfcad'), editable=False, unique=True),
        ),
    ]