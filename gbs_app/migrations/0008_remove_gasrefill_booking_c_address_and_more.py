# Generated by Django 4.1.1 on 2022-11-07 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gbs_app', '0007_rename_adminlogin_userlogin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gasrefill_booking',
            name='c_address',
        ),
        migrations.RemoveField(
            model_name='gasrefill_booking',
            name='cph_no',
        ),
    ]
