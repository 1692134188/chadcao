"""Chad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ChadCao import views
from django.conf.urls import url,include

'''
   path('admin/', admin.site.urls),
   path('index/', views.index, name="index"),  # 创建首页
   path('addStudent/', views.addStudent, name="addStudent"),  # 添加学生
   path('editStudent/(\d+)', views.editStudent, name="editStudent"),  # 编辑学生
   path('delStudent/(\d+)', views.delStudent, name="delStudent"),  # 删除学生
   '''
urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    url(r'^index/$', views.index, name="index"),  # 创建首页
    url(r'^addStudent/$', views.addStudent, name="addStudent"),  # 添加学生
    url(r'^editStudent/(\d+)$', views.editStudent, name="editStudent"),  # 编辑学生
    url(r'^delStudent/(\d+)$', views.delStudent, name="delStudent"),  # 删除学生
]
