from django.conf.urls import url

# from .import views
from django.urls import re_path

from booktest import views
# from booktest.views import index


# 进行url配置师 严格匹配开头和结尾 用 r'网页$'
urlpatterns = [

    # 通过url 函数设置url配置项
    re_path(r'^index/$', views.index),  # 建立index和视图的关系
    re_path(r'^index2/$', views.index2),  # 建立index2和视图的关系
    re_path(r'^books$',views.show_books), # 显示图书信息

    # r'^books/(\d+)$ 正则表达式中 (\d+) 表示会传参数给djandog-->此处传的参数为 bid
    re_path(r'^books/(\d+)$', views.detail) #显示英雄信息

]