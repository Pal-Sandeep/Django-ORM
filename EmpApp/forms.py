from django.forms import models
from .models import Employee

class EmployeeForm(models.ModelForm):

    class Meta:
        model = Employee
        # fields to use in forms
        fields = [
            'first_name',
            'last_name',
            'gender',
            'email',
            'mobile_no',
            'address',
            'joining_date',
        ]
