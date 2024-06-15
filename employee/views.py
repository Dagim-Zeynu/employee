from django.shortcuts import render
from newapp.models import Employee

def home(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees,
    }
    return render(request, 'home.html', context)