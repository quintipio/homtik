# Generated by Django 2.2 on 2019-04-23 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuisine', '0002_auto_20190419_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='recette',
            name='calorie',
            field=models.IntegerField(default=0, verbose_name='Calorique'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recette',
            name='difficulte',
            field=models.IntegerField(default=0, verbose_name='Difficulté'),
            preserve_default=False,
        ),
    ]
