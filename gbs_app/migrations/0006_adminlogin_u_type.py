# Generated by Django 4.1.1 on 2022-11-05 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gbs_app', '0005_rename_u_username_user_details_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminlogin',
            name='u_type',
            field=models.CharField(default=0, max_length=225),
            preserve_default=False,
        ),
    ]