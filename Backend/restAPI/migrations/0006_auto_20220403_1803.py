# Generated by Django 3.2.12 on 2022-04-04 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restAPI', '0005_car_car_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enquiry',
            name='enquiry_number',
        ),
        migrations.AlterField(
            model_name='car',
            name='dealer_abn',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
