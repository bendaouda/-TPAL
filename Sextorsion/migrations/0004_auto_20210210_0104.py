# Generated by Django 3.1.5 on 2021-02-10 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sextorsion', '0003_auto_20210208_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sextorsion',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
