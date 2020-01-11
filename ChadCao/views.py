from django.shortcuts import render, HttpResponse, redirect
from ChadCao.models import Student
from ChadCao.DjangoForms.StudentForm import StudentForm
from django.forms.utils import ErrorDict


# Create your views here.
def index(request):
    student = Student.objects.filter(status="1");
    # locals(变量名称)    可以直接将逻辑处理函数中的所有变量传给模板
    return render(request, "index.html", locals())


def addStudent(request):
    oper = "添加"
    if request.method == "GET":
        student = StudentForm()
        return render(request, "add_editStudent.html", locals())
    else:
        student = StudentForm(request.POST)

        if student.is_valid():
            Student.objects.create(**student.cleaned_data)
            return redirect('/index')
        else:
            return render(request, "add_editStudent.html", {"student": student, "oper": oper})


def editStudent(request, stuID):
    oper = "修改"
    stuData = Student.objects.filter(id=stuID).values().first();
    if not stuData:
        return HttpResponse("您要修改的用户不存在！")
    if request.method == "GET":
        student = StudentForm(stuData)
        if len(dict(student.errors)) == 1 and student.has_error("name", "NameDuplicate"):

            student.errors.clear()
        return render(request, "add_editStudent.html", locals())
    else:
        student = StudentForm(request.POST)
        if student.is_valid():
            Student.objects.filter(id=stuID).update(**student.cleaned_data)
            return redirect('/index')
        else:
            print( str(stuData.get("id")) == str(stuID) , stuData.get("name") == request.POST.get("name"))
            if len(dict(student.errors)) == 1 and student.has_error("name","NameDuplicate"):
                if str(stuData.get("id")) == str(stuID) and stuData.get("name") == request.POST.get("name"):
                    Student.objects.filter(id=stuID).update(**student.cleaned_data)
                    return redirect('/index')
            return render(request, "add_editStudent.html", {"student": student, "oper": oper})


def delStudent(request, stuID):
    student = Student.objects.filter(id=stuID).update(status=False);
    return redirect('/index')
