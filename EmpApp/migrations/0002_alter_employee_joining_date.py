# Generated by Django 4.1.1 on 2022-09-28 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmpApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='joining_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
