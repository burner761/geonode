# Generated by Django 2.2.9 on 2020-01-15 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0029_remove_service_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'base_manager_name': 'objects'},
        ),
    ]
