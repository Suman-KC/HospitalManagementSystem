# Generated by Django 4.2.1 on 2023-06-18 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalmanagement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='doctor',
            new_name='Doctor',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='patient',
            new_name='Patient',
        ),
    ]
