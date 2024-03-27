# Generated by Django 4.1.5 on 2023-01-22 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_clientdetails_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_Counselor', models.CharField(blank=True, max_length=200, null=True)),
                ('KCPA_no_Counselor', models.CharField(blank=True, max_length=200, null=True)),
                ('name_of_Supervisor', models.CharField(blank=True, max_length=200, null=True)),
                ('KCPA_no_Supervisor', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Personal Profile',
            },
        ),
    ]
