# Generated by Django 4.1.1 on 2022-12-10 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gbs_app', '0013_contact_details'),
    ]

    operations = [
        migrations.DeleteModel(
            name='contact_details',
        ),
        migrations.AddField(
            model_name='user_details',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]
