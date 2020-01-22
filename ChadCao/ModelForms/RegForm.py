from django import forms
from ChadCao import models
from django.core.exceptions import ValidationError
import hashlib


# 注册form
class RegForm(forms.ModelForm):
    # 添加确认密码  按照form组件的样式写
    password = forms.CharField(widget=forms.PasswordInput(),
                               label="密码",
                               min_length="6",
                               )
    re_password = forms.CharField(widget=forms.PasswordInput(), label="确认密码")

    class Meta:
        # 指定关联的model
        model = models.User

        # 要展示的内容
        # fields="__all__"   #展示所有的字段
        # exclude=["is_active"] #排除这个字段
        # 或者指定要显示的字段  决定了在页面上的显示顺序 ***  即使是自定义的re_password也可以写进来
        fields = ["username", "name", "password", "re_password", ]

        # 这个label的注释直接在modelform中改 或者 在model中写verbose_name="用户名"
        # 这设置的label只对models里的字段起作用, 自己定义的re_password 不起作用
        labels = {  # 全局设置, 没有加label的字段就还是按数据库里的字段名
            "username": "用户名",
            "password": "密码",
            "name": "姓名",

        }

        widgets = {
            'username': forms.widgets.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.widgets.PasswordInput,
        }

        # 单加的报错 只对title做设置
        error_messages = {
            "username": { "invalid": "格式错误"},
            "password": {  'min_length': '最小长度为6'},
            "re_password": {  'min_length': '最小长度为6'}
        }

        ##初始化把样式调出来

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 调节样式
        print(self.fields)  # 拿到的是对象
        for field in self.fields.values():  # field 是取出来的对象
            field.error_messages = {"required": "不能为空","invalid": "格式错误",'min_length': '最小长度为6'}  # 批量处理
            field.widget.attrs.update({"class": "form-control"})

    def clean(self):  # 两次密码校验
        pwd = self.cleaned_data.get("password")
        re_pwd = self.cleaned_data.get("re_password")
        print(self.cleaned_data)
        if pwd == re_pwd and pwd:  # 如果密码和确认密码一致, 并且存在
            # 两次密码一致 之后对密码进行加密
            md5 = hashlib.md5()  # MD5对象
            md5.update(pwd.encode("utf-8"))  # 加密结果
            pwd = md5.hexdigest()
            print(pwd)  # 3c4423d6a2f6dfcac2ad6f6d1981ad35
            self.cleaned_data["password"] = pwd
            print("-->", self.cleaned_data)
            # {'username': 'sanjiang@qq.com', 'name': 'sanjiang', 'password': '3c4423d6a2f6dfcac2ad6f6d1981ad35', 're_password': 'sanjiang', 'department': <Department: 销售部>, 'mobile': None}
            return self.cleaned_data
        else:
            self.add_error("re_password", "两次密码不一致")  # 把错误提示加到re_password 容易取值
            raise ValidationError("两次密码不一致")  # 错误提示加到了所有的错误里了不容易取值
