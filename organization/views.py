from django.shortcuts import render
from .models import Department, Employee


def department_tree(request):
    departments = Department.objects.all()
    return render(request, 'department_tree.html', {'departments': departments})


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})
