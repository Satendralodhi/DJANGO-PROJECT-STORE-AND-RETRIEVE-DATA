# Generated by Django 5.0.1 on 2024-03-20 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_rename_services_servicess'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='servicess',
            new_name='service',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='taskstatus',
            new_name='mark',
        ),
    ]
