# Generated by Django 2.2.7 on 2020-02-25 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cpanel', '0006_auto_20200224_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinicrating',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='clinicrating',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='hospitalrating',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='hospitalrating',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='labrating',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='labrating',
            name='updated_at',
        ),
    ]
