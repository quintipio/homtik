# Generated by Django 2.2 on 2019-05-02 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuisine', '0010_auto_20190502_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recetteingredient',
            name='unite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuisine.Unite'),
        ),
    ]
