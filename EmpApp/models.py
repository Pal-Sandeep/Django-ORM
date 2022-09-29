# Create your models here.
from django.db import models
from django.contrib import admin


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','gender','email','mobile_no','address','joining_date')

class Employee(models.Model):
    def __str__(self):
        return self.first_name+' '+self.last_name

    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=10,blank=True)
    address = models.CharField(max_length=100,blank=True)
    joining_date = models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=1,default='')
    email = models.EmailField(max_length=256,default='')
    updated_at = models.DateTimeField(auto_now=True)
