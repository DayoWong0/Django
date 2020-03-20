from django.db import models


# 设计和表对应的类 ORM框架 通过类和对象对数据表操作
# 或者根据设计的类生成数据库中的表
# Create your models here.


# 图书类

# 一类
class BookInfo(models.Model):  # 必须继承于model.Model才行
    """图书模型类"""
    # 图书名称 CharField 说明是字符串 max_length指定字符串最大长度
    btitle = models.CharField(max_length=20)
    # 图书出版日期 DateField日期类型
    bpub_date = models.DateField()

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

    hcomment = models.CharField(max_length=128)

    def __str__(self):
        # 返回书名
        return self.hname

    # 关系属性 外键

    # on_delete=models.CASCADE 需要加这个属性
    # 关系属性对应的表的字段名格式: 关系属性名_id

    # 关联对象赋值 直接些外键的名字就可以了

    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)

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
    
    '''

# 数据库 数据表 的增删改查
# https://www.bilibili.com/video/av56977658?p=8
