# Generated by Django 3.2.7 on 2021-09-26 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corona', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coronasettings',
            name='rules',
            field=models.CharField(choices=[('2G', '2G'), ('3G', '3G')], default='2G', max_length=20, verbose_name='Admission rules'),
        ),
    ]
