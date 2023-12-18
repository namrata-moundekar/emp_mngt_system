from rest_framework.routers import SimpleRouter
from .views import *



simple = SimpleRouter()

simple.register('position',PositionCrud)
simple.register('department',DepartmentCrud)
simple.register('employee',EmployeeCrud)


urlpatterns = simple.urls