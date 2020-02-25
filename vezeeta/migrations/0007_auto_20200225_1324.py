# Generated by Django 2.2.7 on 2020-02-25 11:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vezeeta', '0006_auto_20200225_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinicpatientbooking',
            name='booking_date_clinic',
            field=models.DateTimeField(db_column='Booking_Date_clinic', default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='physicianpatientbooking',
            name='booking_date_clinic',
            field=models.DateTimeField(db_column='Booking_Date_clinic', default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='physicianpatientbooking',
            name='booking_date_hospital',
            field=models.DateTimeField(db_column='Booking_Date_Hospital', default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]