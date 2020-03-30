
from django.http import HttpResponse


class BlockedIPSMiddleware(object):
    EXCLUDE_IPS = ['127.0.0.1'] # 禁止ip列表
    def process_view(self,request, view_func, *view_args, **view__kwargs):
            user_ip = request.META['REMOTE_ADDR']
            if user_ip in self.EXCLUDE_IPS:
                return HttpResponse('你不配访问本网站') 
            # else:
            #     return view_func(request, *view_args, **view_kwargs)

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
            return self.get_response(request)


class TestMiddleware(object):
    "中间件类"

    def __init__(self, get_response):
        self.get_response = get_response
        # 服务器重启之后,接收第一个请求时调用
        print('----init----')

    def __call__(self, request):
            return self.get_response(request)
    # def __init__(self):
    #     # 服务器重启之后,接收第一个请求时调用
    #     print('----init----')

    def process_request(self, request, view_func,*view_args,**view__kwargs):
        # 产生request对象之后,url匹配之前调用
        print('--process_request-----')

    def process_view(self, request, view_func,*view_args,**view__kwargs):
    #url匹配之后 视图函数调用之前
        print('process_view')
    
    def process_response(self, request, response):
        "视图函数调用之后,内容返回之前"
        print('--process_response')
        return response


class ExceptionTest1Middleware(object):
    def process_exception(self, request, exception):
        "view异常时调用"
        print('--process_exception1')

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
            return self.get_response(request)

class ExceptionTest2Middleware(object):
    def process_exception(self, request, exception):
        "view异常时调用"
        print('--process_exception2')

    def __init__(self, get_response):
       self.get_response = get_response

    def __call__(self, request):
            return self.get_response(request)





