# Generated by Django 2.2 on 2019-05-03 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuisine', '0018_auto_20190503_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseautre',
            name='achete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='courseingredient',
            name='achete',
            field=models.BooleanField(default=False),
        ),
    ]
