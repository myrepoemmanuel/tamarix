# Generated by Django 3.1.7 on 2021-05-30 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210514_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
