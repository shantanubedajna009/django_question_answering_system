# Generated by Django 2.2.3 on 2020-04-07 16:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('qsapp', '0007_auto_20200407_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='atag',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
