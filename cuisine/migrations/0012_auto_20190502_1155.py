# Generated by Django 2.2 on 2019-05-02 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuisine', '0011_auto_20190502_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unite',
            name='unite_mere',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cuisine.Unite'),
        ),
    ]