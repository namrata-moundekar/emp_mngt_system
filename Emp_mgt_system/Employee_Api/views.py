from Employee.models import Employee, Position, Department
from .serializers import EmployeeSerializer, PositionSerializer, DepartmentSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ReadOnlyModelViewSet


# Create your views here.
class PositionCrud(ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class DepartmentCrud(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeCrud(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer





