from django.contrib import admin
from .models import Employee, EmployeeAdmin

admin.site.register(Employee,EmployeeAdmin)

# Register your models here.
