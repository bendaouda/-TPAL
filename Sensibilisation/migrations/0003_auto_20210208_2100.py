# Generated by Django 3.1.5 on 2021-02-08 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sensibilisation', '0002_auto_20210208_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensibilisation',
            name='contenu',
            field=models.TextField(null=True),
        ),
    ]
