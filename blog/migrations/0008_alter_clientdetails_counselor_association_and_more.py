# Generated by Django 4.1.5 on 2023-01-22 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_personalprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdetails',
            name='counselor_Association',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='clientdetails',
            name='supervisor_Association',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]