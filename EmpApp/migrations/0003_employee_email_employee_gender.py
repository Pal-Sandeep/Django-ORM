# Generated by Django 4.1.1 on 2022-09-29 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmpApp', '0002_alter_employee_joining_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(default='', max_length=1),
        ),
    ]
