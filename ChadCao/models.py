from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField('学生姓名',max_length=200,blank=True,null=True)
    age=models.IntegerField('年龄',default=18)
    status =models.IntegerField('状态',default=1)