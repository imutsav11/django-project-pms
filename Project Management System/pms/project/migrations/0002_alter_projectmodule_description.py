# Generated by Django 5.0.1 on 2024-02-22 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmodule',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]