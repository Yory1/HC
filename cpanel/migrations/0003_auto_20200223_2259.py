# Generated by Django 2.2.7 on 2020-02-23 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpanel', '0002_auto_20200220_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinicrating',
            name='rate',
            field=models.IntegerField(blank=True, db_column='rate', null=True),
        ),
        migrations.AddField(
            model_name='hospitalrating',
            name='rate',
            field=models.IntegerField(blank=True, db_column='rate', null=True),
        ),
        migrations.AddField(
            model_name='labrating',
            name='rate',
            field=models.IntegerField(blank=True, db_column='rate', null=True),
        ),
        migrations.AddField(
            model_name='physicianrating',
            name='rate',
            field=models.IntegerField(blank=True, db_column='rate', null=True),
        ),
        migrations.AlterField(
            model_name='medicalinstitutions',
            name='image',
            field=models.ImageField(blank=True, db_column='Image', default='image.png', null=True, upload_to='Medical_Institutions/images'),
        ),
    ]
