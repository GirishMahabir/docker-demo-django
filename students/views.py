from django.shortcuts import render, redirect
from students.models import Student
from students.forms import StudentForm

# Create your views here.
def stud(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view')
            except:
                pass
    else:
        students = StudentForm()
        form = StudentForm()
    
    return render(request, 'index.html', {'form': form})

def view(request):
    students = Student.objects.all()
    return render(request, 'view.html', {'students': students})

def edit(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'edit.html', {'student': student})

def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/view')
