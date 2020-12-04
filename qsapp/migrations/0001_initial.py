# Generated by Django 2.2.3 on 2020-04-05 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('recID', models.AutoField(primary_key=True, serialize=False)),
                ('answer', models.CharField(blank=True, max_length=255)),
                ('atag', models.CharField(blank=True, max_length=255, unique=True)),
                ('comment', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('recID', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(blank=True, max_length=255)),
                ('atag', models.ForeignKey(db_column='atag', on_delete=django.db.models.deletion.CASCADE, to='qsapp.Answers', to_field='atag')),
            ],
        ),
    ]