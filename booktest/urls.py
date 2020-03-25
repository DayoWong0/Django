from django.conf.urls import url

# from .import views
from django.urls import re_path

from booktest import views

# from booktest.views import index


# 进行url配置师 严格匹配开头和结尾 用 r'网页$'
urlpatterns = [

    # 通过url 函数设置url配置项
    re_path(r'^index666/$', views.index666),  # 建立index和视图的关系
    re_path(r'^index2/$', views.index2),  # 建立index2和视图的关系
    re_path(r'^books$', views.show_books),  # 显示图书信息

    re_path(r'^index/$', views.index),  # 建立index和视图的关系
    re_path(r'^create/$', views.create),  # 增加图书
    re_path(r'^delete(\d+)$', views.delete),  # 删除图书

    # r'^books/(\d+)$ 正则表达式中 (\d+) 表示会传参数给djandog-->此处传的参数为 bid
    re_path(r'^books/(\d+)$', views.detail),  # 显示英雄信息

    re_path(r'^areas/$', views.areas),  # 自关联案例

    re_path(r'^indexView/$', views.indexView),  # 建立index和视图的关系
    re_path(r'^login/$', views.login),  # 建立index和视图的关系
    re_path(r'^login_check$', views.login_check),  # 建立index和视图的关系

    re_path(r'^test_ajax$', views.ajax_test),  # 建立index和视图的关系
    re_path(r'^ajax_handle$', views.ajax_handle),  # 建立index和视图的关系
    re_path(r'^login_ajax$', views.login_ajax),  # 建立index和视图的关系
    re_path(r'^login_ajax_check$', views.login_ajax_check),  # ajax登录校验

    re_path(r'^get_cookie/$', views.get_cookie),  # 获取cookie
    re_path(r'^set_cookie/$', views.set_cookie),  # 设置cookie

    re_path(r'^set_session/$', views.set_session),  # 设置session
    re_path(r'^get_session/$', views.get_session),  # 获取session


    

]


