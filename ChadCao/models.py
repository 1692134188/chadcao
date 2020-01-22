from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Student(models.Model):
    name = models.CharField('学生姓名', max_length=200, blank=True, null=True)
    age = models.IntegerField('年龄', default=18)
    status = models.IntegerField('状态', default=1)


class User(models.Model):
    username = models.EmailField(
        max_length=255,
        unique=True,
    )
    name = models.CharField('名字', max_length=32)
    password = models.CharField('密码', max_length=64)
    class Meta:
        verbose_name = '账户信息'
        verbose_name_plural = "账户信息"

    def __str__(self):  # __unicode__ on Python 2
        return self.username
