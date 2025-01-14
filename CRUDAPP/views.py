from django.shortcuts import render, redirect
from CRUDAPP.models import Employee

# for trigger
from django.http import HttpResponse



# Create Employee

def insert_emp(request):
    if request.method == "POST":
        EmpId = request.POST['EmpId']
        EmpName = request.POST['EmpName']
        EmpGender = request.POST['EmpGender']
        EmpEmail = request.POST['EmpEmail']
        EmpDesignation = request.POST['EmpDesignation']
        data = Employee(EmpId=EmpId, EmpName=EmpName, EmpGender=EmpGender, EmpEmail=EmpEmail, EmpDesignation= EmpDesignation)
        data.save()
  
        return redirect('show/')
    else:
        return render(request, 'insert.html')



# Retrive Employee
        
def show_emp(request):
    employees = Employee.objects.all()
    return render(request,'show.html',{'employees':employees} )



# Update Employee

def edit_emp(request,pk):
    employees = Employee.objects.get(id=pk)
    if request.method == 'POST':
        return redirect('/show')

    context = {
        'employees': employees,
    }

    return render(request,'edit.html',context)


# Delete Employee

def remove_emp(request, pk):
    employees = Employee.objects.get(id=pk)

    if request.method == 'POST':
        employees.delete()
        return redirect('/show')

    context = {
        'employees': employees,
    }

    return render(request, 'delete.html', context)

# Sample Trigger Button 

def home(request):
    context = {
        "title" : "Trigger Python Logic"
    }
    return render(request, "home.html",context)

def simple_function(request):

    num = 0
    if num == 2:
         print("\n This is a simple function \n")
    else:
         print("\n This is a simple function 2 \n")

   
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")

