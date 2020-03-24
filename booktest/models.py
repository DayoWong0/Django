from django.db import models


# 设计和表对应的类 ORM框架 通过类和对象对数据表操作
# 或者根据设计的类生成数据库中的表
# Create your models here.


class BookInfoManage(models.Manager):  # 自定义管理类
        #     1.改变查询结果集
    def all(self):
        #         调用父类all方法 获取所有
        books = super().all()  # 查询集合
        #     对数据进行过滤
        books = books.filter(isDelete=False)
        return books

    # 2.封装函数:操作模型类对应的数据表(增删改查)
    def create_book(self, btitle, bpub_date):
        #获取self所在模型类
        model_class = self.model
        # creat book对象
        book = model_class()
        # book = BookInfo() #这个就不用了
        book.btitle = btitle
        book.bpub_date = bpub_date
        # 保存
        book.save()
        # 返回book
        return book








# 返回books


# 图书类

# 一类
class BookInfo(models.Model):  # 必须继承于model.Model才行
    """图书模型类"""
    # 图书名称 CharField 说明是字符串 max_length指定字符串最大长度
    btitle = models.CharField(max_length=20)
    # 图书出版日期 DateField日期类型
    bpub_date = models.DateField()
    # 阅读量
    bread = models.IntegerField(default=0)
    # 评论量
    bcomment = models.IntegerField(default=0)
    # 删除标记 不做真正的删除 软删除
    isDelete = models.BooleanField(default=False)
    # 加这个可以使用BookInfo.object. 不加不行
    objects = BookInfoManage()  # 管理类 自定义

    # 指定数据表表名
    class Meta:
        db_table = '表名'

    @classmethod
    def creat_book(cls,btitle,bpub_date):
        obj = cls()
        obj.btitle = btitle
        obj.bpub_date = bpub_date
    #     保存
        obj.save()
        return obj

    def __str__(self):
        # 返回书名
        return self.btitle


#     primary key自动生成--对应为类名

# 多类
class HeroInfo(models.Model):
    """英雄人物类书籍  和图书模型类有关系"""
    hname = models.CharField(max_length=20)  # 姓名

    # 性别 Boolean bool类型 default指定默认值 false代表男
    hgender = models.BooleanField(default=False)
    # 备注
    hcomment = models.CharField(max_length=128)
    # 关系属性 外键
    # on_delete=models.CASCADE 需要加这个属性
    # 关系属性对应的表的字段名格式: 关系属性名_id
    # 关联对象赋值 直接些外键的名字就可以了
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    # 删除标记 不做真正的删除 软删除
    isDelete = models.BooleanField(default=False)

    # 加这个可以使用BookInfo.object. 不加不行
    objects = models.Manager()

    def __str__(self):
        # 返回书名
        return self.hname


class AreaInfo(models.Model):
    """地区模型类"""
    # 地区名称
    atitle = models.CharField(max_length=20)
    #     关系属性,代表当前地区父级地区 自关联
    aParent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)  # null数据库里可为空, blank管理页面可为空
    objects = models.Manager()

    def __str__(self):
        return self.atitle


"""
#   两个表都是空的     

# 对b赋值
>>> from booktest.models import BookInfo,HeroInfo
>>> b = BookInfo()
>>> b.btitle = '天龙八部'
>>> b.bpub_date = date(1990,1,1)
>>> from datetime import date
>>> b.bpub_date = date(1990,1,1)
>>> b.save()
>>> b.btitle
'天龙八部'
>>> b.bpub_date
datetime.date(1990, 1, 1)

# 对h赋值
>>> h = HeroInfo()
>>> h.hname = '张雄'
>>> h.hgender = False
>>> h.hcomment = '66666'

# 外键对应关系表示
>>> h.hbook = b
>>> h.save()

"""

"""关系操作查询

https://www.bilibili.com/video/av56977658?p=9

>>> h3.hbook
<BookInfo: BookInfo object (2)>

>>> h3.hbook.btitle
'天龙八部'

>>> b.heroinfo_set.all()

<QuerySet [<HeroInfo: HeroInfo object (1)>, <HeroInfo: HeroInfo object (2)>]>




"""
'''

# 数据表生成

1.生成迁移文件

命令参考:

https://code.ziqiangxuetang.com/django/django-basic.html

python manage.py makemigrations

(Django) zxdeMacBook-Pro:mysite zx$ python manage.py makemigrations
Migrations for 'booktest':
  booktest/migrations/0001_initial.py
    - Create model BookInfo
    
    


2.执行迁移生成表 python manage.py migrate
    
    
    
    
一起执行:

python manage.py makemigrations
python manage.py migrate   

    
    '''

# 数据库 数据表 的增删改查
# https://www.bilibili.com/video/av56977658?p=8
