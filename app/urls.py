from django.contrib import admin
from django.urls import path

from organization import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('department_tree/', views.department_tree, name='department_tree'),
    path('employee_list/', views.employee_list, name='employee_list'),
]
