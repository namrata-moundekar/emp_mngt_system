# Generated by Django 4.2.7 on 2023-12-17 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0006_alter_employee_code_alter_employee_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]