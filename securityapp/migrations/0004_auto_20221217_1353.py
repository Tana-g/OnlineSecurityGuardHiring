# Generated by Django 3.1.3 on 2022-12-17 08:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('securityapp', '0003_register'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Register',
            new_name='Profile',
        ),
    ]
