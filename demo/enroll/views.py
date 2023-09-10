from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.
# add new data in student table
def add(request):
    if request.method == 'POST':
        fm =  StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            reg = User(name=name, email=email, password=password)
            reg.save()
            fm =  StudentRegistration()
    else:
        fm =  StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/add.html', {'form':fm, 'stu': stud})

# delete function
def delete(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

# edit function
def update(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm =  StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm =  StudentRegistration(instance=pi) 
    return render(request, 'enroll/update.html', {'form':fm})
