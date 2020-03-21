from datetime import date

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from booktest.models import BookInfo  # 导入图书模型类
from django.template import loader, RequestContext

# Create your views here.

# 定义视图函数

# 必须有request参数
# 127.0.0.1:8080/index
from booktest.models import BookInfo


# def index(request):
#     # 进行处理,和M 和 T 进行交互
#     # # return HttpResponse('老铁 没毛病aaaaaaa')
#     #
#
#
#     # 使用模板文件
#     #
#     # 1.加载模板文件 这里目录填相对于templates
#     temp = loader.get_template('booktest/index666.html')
#
#     # Djandog3.0版本 必须传入一个字典给 render()函数
#     # 2.定义模板上下文:给模板文件传递数据 给变量传值等
#     # context = RequestContext({})
#
#     context = {}
#
#     # 3.模板渲染:产生标准的html
#     res_html = temp.render(context)
#     # 4.返回浏览器
#     return HttpResponse(res_html)

# 传值给网页
def index666(request):
    con = {'content': 'Mike', 'list': list(range(1, 10))}
    return render(request, 'booktest/index666.html', con)


# 127.0.0.1:8080/index2
def index2(request):
    return HttpResponse('index 2')


def show_books(request):
    """显示图书信息"""
    books = BookInfo.objects.all()
    return render(request, 'booktest/show_books.html', {'books': books})


def detail(request, bid):
    """查询图书关联的英雄信息"""

    # 1.根据id查询图书信息
    book = BookInfo.objects.get(id=bid)
    #     查询和book关联的英雄信息
    heros = book.heroinfo_set.all()
    #     传递数据给模板
    return render(request, 'booktest/detail.html', {'book': book, 'heros': heros})


def index(request):
    """显示图书信息"""
    # 1.查询信息
    books = BookInfo.objects.all()
    # 2.使用模板
    return render(request, 'booktest/index.html',
                  {'books': books})


def create(request):
    #     新增一本书
    b = BookInfo()
    b.btitle = '我爱你'
    b.bpub_date = date(1990, 1, 1)
    # 保存到数据库
    b.save()
    return HttpResponse('ok')

    # 重定向到首页     返回到index页面
    # return HttpResponseRedirect('/index')


def delete(request, bid):
    """删除图书"""
    # 获取图书id
    book = BookInfo.objects.get(id=bid)
    book.delete()
    
    # 重定向 
    # return HttpResponseRedirect('/index')
    # 简单写法
    return redirect('/index') 

