from datetime import date

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from booktest.models import BookInfo, AreaInfo  # 导入图书模型类
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
    # return HttpResponse('ok')

    # 重定向 
    # return HttpResponseRedirect('/index')
    # 简单写法
    return redirect('/index')


def delete(request, bid):
    """删除图书"""
    # 获取图书id
    book = BookInfo.objects.get(id=bid)
    book.delete()

    # 重定向 
    # return HttpResponseRedirect('/index')
    # 简单写法
    return redirect('/index')


def areas(request):
    """获取广州市的上下级地区"""
    #     获取广州的信息
    area = AreaInfo.objects.get(atitle='广州市')

    #     查询广州市的上级地区,两种方法
    #     aParent = AreaInfo.objects.get(aParent='广州市')
    #   第二种方法, 由多查1模型  p25讲解的例子
    parent = area.aParent
    #     查询广州市的下级地区
    children = area.areainfo_set.all()
    #     模板
    return render(request, 'booktest/areas.html',
                  {'area': area, 'parent': parent, 'children': children})


def indexView(request):
    """首页"""
    return render(request, 'booktest/indexView.html')


def login(request):
    """显示登录页面"""
    # 判断用户是否登录
    if request.session.has_key('islogin'):
        # 用户已登录
        return redirect('/index666')


    # 获取cookie username
    if 'username' in request.COOKIES:
        # 获取用户名
        username = request.COOKIES['username']
    else:
        username = ''


    return render(request, 'booktest/login.html', {'username':username})


def login_check(request):
    """ request.POST,GET 分别保存对应方法提交的参数"""

    """登录验证"""
    '''1.获取账号密码'''
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')

    # print(username,password,remenmber)
    '''2.验证密码是否正确'''
    # 用户名,密码:zx zx 正确跳转 不正确继续登录
    if username == 'zx' and password == 'zx':
        # 正确跳转
        response = redirect('/index666')
        # 判断是否需要记住用户名
        if remember == 'on':
            # 过期时间 一周
            response.set_cookie('username',username,max_age=7*24*3600)
        
        # 记住用户登录状态
        # session 有islogin就认为用户已经登录
        request.session['islogin'] = True

        return response



    else:
        # return redirect('/login')
        return HttpResponse('登录失败')


def ajax_test(request):
    return render(request, 'booktest/test_ajax.html')


def ajax_handle(request):
    """ajax请求处理"""

    return JsonResponse({'res': '1'})

def login_ajax(request):
    return render(request, 'booktest/login_ajax.html')

   # /login_ajax_check
def login_ajax_check(request):
    """ajax登录校验"""

    """ request.POST,GET 分别保存对应方法提交的参数"""

    """登录验证"""
    '''1.获取账号密码'''
    username = request.POST.get('username')
    password = request.POST.get('password')
    # print(username,password)
    '''2.验证密码是否正确'''
    # 用户名,密码:zx zx 正确跳转 不正确继续登录
    if username == 'zx' and password == 'zx':
        # 正确,返回json数据
        # return redirect('/index666')
        return JsonResponse({'res':1})
    else:
        # return redirect('/login')
        return JsonResponse({'res':0})
# /set_cookie
def set_cookie(request):
    '设置cookie信息'
    response = HttpResponse('设置cookie')
    # 设置一个cookie信息 名字为mum 值为1

    # maxage 多少秒后到期,expires 具体时间到期
    response.set_cookie('num',6, max_age=14*24*3600)
    # response.set_cookie('num',6, expires=)

    return response

# /get_cookie
def get_cookie(request):
    '获取cookie'
    # 取出cookie num的值
    num = request.COOKIES['num']
    return HttpResponse(num)


def set_session(request):
    # 设置session
    request.session['username'] = 'smart'
    request.session['age'] = 18
    request.session.set_expiry(600)

    return HttpResponse('设置session,过期时间600秒')

def get_session(request):
    # 设置session
    username = request.session['username']
    age = request.session['age']

    # HttpResponse()里面的参数拼接 需要用加号
    return HttpResponse('获取session:'+username+':'+str(age))

def clear_session(request):
    "清除session 删除值的部分"
    request.session.clear()
    return HttpResponse('清除成功')










