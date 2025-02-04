# Generated by Django 3.2.6 on 2021-08-05 09:27

from django.db import migrations, models
import registration.models.event


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0046_auto_20210523_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='gifts',
            field=models.BooleanField(default=False, verbose_name='Manage gifts and presence for helpers'),
        ),
        migrations.AlterField(
            model_name='event',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=registration.models.event._logo_upload_path, verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='event',
            name='logo_social',
            field=models.ImageField(blank=True, help_text='Best results with 1052 x 548 px.', null=True, upload_to=registration.models.event._logo_upload_path, verbose_name='Logo for Facebook'),
        ),
    ]
