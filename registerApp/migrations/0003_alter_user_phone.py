# Generated by Django 3.2.2 on 2021-05-10 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerApp', '0002_auto_20210510_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(max_length=12),
        ),
    ]