from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from employee.forms import EmployeeForm
from employee.models import Employee


# Create your views here.
def show(request):
    employees = Employee.objects.all()
    return render(request, 'employee/show.html', {'employees': employees})


def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'employee/index.html', {'form': form})
