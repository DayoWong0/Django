from django.contrib import admin
from .models import BookInfo, HeroInfo, AreaInfo

# Register your models here.

# 创建管理员账号
"""

python manage.py createsuperuser
 
# 按照提示输入用户名和对应的密码就好了邮箱可以留空，用户名和密码必填
 
# 修改 用户密码可以用：
python manage.py changepassword username

"""


# 自定义模型管理类
class BookInfoAdmin(admin.ModelAdmin):
    """图书模型管理类"""
    list_display = ['id', 'btitle', 'bpub_date','title']
    list_per_page = 10 #每页显示10条数据
    actions_on_bottom = True
    # actions_on_top = False
    list_filter = ['bpub_date'] #界面右侧过滤栏
    search_fields = ['btitle'] #以bittle搜索框

    # fields = ['bpub_date','btitle']
    fieldsets = (
        ('基本', {'fields':['btitle']}),
        ('高级', {'fields':['bpub_date']})
    )








class HeroInfoAdmin(admin.ModelAdmin):
    """英雄人物模型管理类"""
    list_display = ['id', 'hname', 'hcomment']

class AreasAdmin(admin.ModelAdmin):
    """英雄人物模型管理类"""
    list_display = ['atitle', 'aParent']


# 注册模型类
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
admin.site.register(AreaInfo, AreasAdmin)
