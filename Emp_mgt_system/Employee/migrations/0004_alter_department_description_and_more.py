# Generated by Django 4.2.7 on 2023-12-16 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0003_alter_department_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
