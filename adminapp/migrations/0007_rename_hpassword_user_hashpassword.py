# Generated by Django 4.0.4 on 2022-05-30 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0006_rename_phone_user_name_remove_user_status_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='hpassword',
            new_name='hashpassword',
        ),
    ]