# Generated by Django 4.2.7 on 2023-12-17 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0005_alter_employee_email_alter_employee_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='code',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]