# Generated by Django 2.2 on 2019-05-02 12:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuisine', '0012_auto_20190502_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='recette',
            name='categorie',
            field=models.PositiveIntegerField(choices=[(1, 'Entrée'), (2, 'Plat'), (3, 'Dessert')], default=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)], verbose_name='Catégorie'),
        ),
    ]
