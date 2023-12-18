# Generated by Django 4.2.7 on 2023-12-16 09:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'DEPARTMENT_INFO',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'POSITION_INFO',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('salary', models.FloatField(default=0)),
                ('email', models.TextField()),
                ('dob', models.DateField(blank=True, null=True)),
                ('gender', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('male', 'male'), ('female', 'female')], max_length=11, null=True, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('upload_file', models.FileField(blank=True, null=True, upload_to='Pdf_files/', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('status', models.IntegerField()),
                ('phone', models.TextField()),
                ('hire_date', models.DateField()),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.department')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.position')),
            ],
            options={
                'db_table': 'EMPLOYEE_INFO',
            },
        ),
    ]