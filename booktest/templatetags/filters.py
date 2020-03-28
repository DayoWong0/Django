# 自定义过滤器
# 过滤器 = python函数

from django.template import Library

# 创建library对象
register = Library()

@register.filter
def mod(num):
# 判断偶数
    return num%2 == 0

