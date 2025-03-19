from django.shortcuts import render, redirect
from . models import Student
from django.db.models import Q
# Create your views here.


def home(request):
    all_stdudent = Student.objects.all()

    if request.method == 'GET':
        data = request.GET.get('src')
        if data:
            all_stdudent = Student.objects.filter(Q(name__icontains = data) | Q(email__icontains = data))
            print(all_stdudent)

    return render(request, 'index.html',{'stu': all_stdudent})


def delete_prof(request, id):
    all_stdudent = Student.objects.get(id=id)
    all_stdudent.delete()
    return redirect(home)