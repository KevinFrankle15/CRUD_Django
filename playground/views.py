from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# handling req and response
# action

def say_started(request):
    return HttpResponse('server started,WELCOME TO LOGIN PAGE')
# using Templates
def templates(request):
    return render(request,'template.html')
# for debugging test 
def debug():
    x=1
    y=2
    return x + y

# For CURD operation :

def emp_list(request):
    return render(request,'employee_register/emp_list.html')

def emp_form(request):
    return render(request,'employee_register/emp_form.html')

def emp_delete(request):
    return