# Generated by Django 5.1 on 2024-10-05 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statectl', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Server',
            new_name='StatectlServer',
        ),
    ]
