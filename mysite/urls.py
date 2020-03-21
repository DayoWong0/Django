"""mysite URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path

import booktest
from booktest import urls, views

urlpatterns = [
    # path('polls/', include('polls.urls')),
    path('002d4248-7dd7-4b24-ac0c-46df0dde9ee2/', admin.site.urls),  # 配置项目
    # path('index/', include('booktest.urls'))

    # 正则表达式匹配
    re_path(r'^', include('booktest.urls'))  # 包含booktest应用中的urls文件
]
