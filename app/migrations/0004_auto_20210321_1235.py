# Generated by Django 2.2 on 2021-03-21 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210321_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(default='Enter a short description.', max_length=20),
        ),
    ]