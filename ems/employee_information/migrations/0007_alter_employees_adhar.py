# Generated by Django 4.2 on 2023-04-27 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0006_employees_adhar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='Adhar',
            field=models.IntegerField(),
        ),
    ]
