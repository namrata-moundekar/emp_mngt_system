"""
URL configuration for Emp_mgt_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Employee import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='EMPLOYEE SERVICE')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dash/', views.dashboard_page,name='dash'),

    path('emp/', views.add_or_update_emp, name='add_or_update_emp'),
    path('emp/<int:emp_id>/', views.add_or_update_emp, name='add_or_update_emp'),
    path('delete_emp/<int:emp_id>/', views.delete_emp, name='delete_emp'),

    path('dept/', views.add_or_update_dept, name='add_or_update_dept'),
    path('dept/<int:dept_id>/', views.add_or_update_dept, name='add_or_update_dept'),
    path('delete_dept/<int:dept_id>/', views.delete_dept, name='delete_dept'),

    path('role/', views.add_or_update_role, name='add_or_update_role'),
    path('role/<int:role_id>/', views.add_or_update_role, name='add_or_update_role'),
    path('delete_role/<int:role_id>/', views.delete_role, name='delete_role'),

    path('emp-service/',include('Employee_Api.urls')),
    path('swagger/', schema_view),
    path('apis/', include('rest_framework.urls')),

    # Add other URL patterns as needed
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




