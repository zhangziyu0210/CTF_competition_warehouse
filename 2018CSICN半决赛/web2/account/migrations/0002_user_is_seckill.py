# Generated by Django 2.0.5 on 2018-05-20 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_seckill',
            field=models.BooleanField(default=False),
        ),
    ]
