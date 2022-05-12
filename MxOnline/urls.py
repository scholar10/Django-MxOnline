"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include,re_path
from django.views.generic import TemplateView
from django.views.static import serve #处理静态文件的
from MxOnline.settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name="index"), #一般纯静态页面使用这种形式
    #re_path('^login/$', TemplateView.as_view(template_name="login.html"), name="login")
    path('', include(('organization.urls','organization'),namespace="organization")),
    path('', include(('users.urls','users'),namespace="users")),

    path('captcha/', include('captcha.urls')),#验证码

    #配置上传文件的访问处理函数
    re_path(r'^media/(?P<path>.*)$',serve,{"document_root":MEDIA_ROOT})
]
