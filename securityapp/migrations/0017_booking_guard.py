# Generated by Django 3.1.3 on 2022-12-24 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('securityapp', '0016_auto_20221223_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='guard',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='securityapp.guard'),
        ),
    ]