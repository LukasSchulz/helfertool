# Generated by Django 3.2.3 on 2021-05-23 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0004_auto_20210423_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
