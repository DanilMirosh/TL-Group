from django.contrib import admin
from .models import Department, Employee


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_department')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'hire_date', 'salary', 'department')


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
