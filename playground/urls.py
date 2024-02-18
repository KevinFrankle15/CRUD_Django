from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.templates), # calling function reference
    path('employee-list/',views.emp_list),
    path('employee-form/',views.emp_form),
]