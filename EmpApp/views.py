# from http.client import HTTPResponseRedirect
from django.shortcuts import redirect, render,get_object_or_404,HttpResponseRedirect
from .models import Employee
from .forms import EmployeeForm
from django.contrib import messages
def index(request):
    Emps = Employee.objects.all().order_by('id')
    return render(request,'index.html',{'Emps':Emps}) 
    
def create_view(request):
    context = {}
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
         form.save()
         return redirect("/create")
        #  return HttpResponseRedirect("/")   #just trying to redirect to home page if error delete this
    messages.success(request, "Employee Added Successfully")
    context['form']=form
    return render(request,'create_view.html',context)

def delete_Emp(request,id):
    obj = get_object_or_404(Employee,id=id)

    if request.method =="POST":
        obj.delete()

        return HttpResponseRedirect("/")
    messages.success(request, "Employee Deleted Successfully")
    return render(request,"delete_Emp.html")

def updateEmp(request,pk):
    emp = Employee.objects.get(id=pk)
    if request.method=='POST':
        emp = Employee.objects.get(id = pk)
        emp.first_name = request.POST.get('first_name')
        emp.last_name = request.POST.get('last_name')
        emp.email = request.POST.get('email')
        emp.mobile_no = request.POST.get('mobile_no')
        emp.gender = request.POST.get('gender')
        emp.address = request.POST.get('address')
        emp.save()
        messages.success(request, "Employee Update Successfully")
        return redirect('/')


    return render(request,'updateEmp.html',{'emp':emp})