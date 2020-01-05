from django.shortcuts import render,HttpResponse,redirect
from ChadCao.models import Student
# Create your views here.
def index(request):
    student = Student.objects.all();
    # locals(变量名称)    可以直接将逻辑处理函数中的所有变量传给模板
    return render(request,"index.html",locals())
def addStudent(request):
    if request.method=="GET":
        return render(request, "addStudent.html", locals())
    name=request.POST.get('name')
    age=int(request.POST.get('age'))
    Student.objects.create(name=name,age=age)
    return redirect('/index')

def editStudent(request,stuID):
    student = Student.objects.get(id=stuID);
    if request.method == "GET":
        return render(request, "editStudent.html", locals())
    student.name = request.POST.get('name')
    student.age = int(request.POST.get('age'))
    student.save()
    return redirect('/index')
def delStudent(request,stuID):
    student = Student.objects.get(id=stuID).delete();
    return redirect('/index')
