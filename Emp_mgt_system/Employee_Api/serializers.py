from Employee.models import Employee, Position, Department
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class EmployeeSerializer(ModelSerializer):
    position = serializers.StringRelatedField()
    dept = serializers.StringRelatedField()

    class Meta:
        model = Employee
        fields = '__all__'


class PositionSerializer(ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'










