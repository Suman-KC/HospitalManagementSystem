# Generated by Django 4.2.1 on 2023-06-20 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalmanagement', '0004_alter_users_mobile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='Contact',
        ),
    ]
