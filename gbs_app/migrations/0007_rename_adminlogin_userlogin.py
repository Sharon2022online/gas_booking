# Generated by Django 4.1.1 on 2022-11-05 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gbs_app', '0006_adminlogin_u_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='adminlogin',
            new_name='userlogin',
        ),
    ]
