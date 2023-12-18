from django.db import models
from django.core.validators import FileExtensionValidator, MinValueValidator
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]

class Department(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'DEPARTMENT_INFO'


class Position(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'POSITION_INFO'


class Employee(models.Model):
    code = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    salary = models.FloatField(default=0)
    email = models.EmailField(max_length=254)
    dob = models.DateField(blank=True, null=True)
    gender = MultiSelectField(choices=GENDER_CHOICES, null=True, blank=True, validators=[MinValueValidator(0.0)])
    upload_file = models.FileField(upload_to='images/', null=True, blank=True,validators=[FileExtensionValidator(['pdf'])])
    status = models.CharField(max_length=50)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='employees')
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    phone = PhoneNumberField()
    hire_date = models.DateField()

    def __str__(self):
        return self.first_name + ' '+self.last_name + ' '

    class Meta:
        db_table = 'EMPLOYEE_INFO'
