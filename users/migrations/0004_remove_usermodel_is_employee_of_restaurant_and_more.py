# Generated by Django 4.2.4 on 2024-07-23 07:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_usermodel_is_employee_of_restaurant"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usermodel",
            name="is_employee_of_restaurant",
        ),
        migrations.RemoveField(
            model_name="usermodel",
            name="is_restaurant",
        ),
    ]
