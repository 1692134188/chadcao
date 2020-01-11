# 创建学生的DjangoForm
from django import forms
from django.forms import fields
from ChadCao.models import Student
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError


class StudentForm(forms.Form):
    name = forms.CharField(
        label="姓名",
        required=True,
        max_length=20,
        min_length=2,
        error_messages={
            "required": "姓名不能为空！",
            "min_length": "姓名的长度不能小于2位",
            "max_length": "姓名的长度不能超过20位"
        }
    )
    age = forms.IntegerField(
        label="年龄",
        required=True,
        max_value=200,
        min_value=3,
        error_messages={
            "required": "年龄不能为空！",
            "min_value": "年龄的不能小于3岁",
            "max_value": "年龄的不能超过200岁"
        }
    )
    status = forms.HiddenInput(
    )

    def clean_name(self):
        curName = self.cleaned_data["name"]
        stuList=Student.objects.filter(name=curName,status=True)
        if stuList:
            raise ValidationError(message='姓名已存在!', code='NameDuplicate')
        return curName
