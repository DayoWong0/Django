# Django
Django学习

## Test  
Markdown  

    注意点1:  
    配置网站地址 统一加 /  
    
    1. /creat
    这种网址是: 域名 + 路径
    
    2. create
    这种是 当前页面的路径 拼接 creat,当出现 / 的时候 会出问题
    
    urls.py配置 末尾统一加 '/' 
    html中 地址开头统一用 '/create'这样的就行了
    一头一尾
    

##数据库

###django选项(models.py 导入的models包内)  
    DecimalField() 比FloatField()精确 FloatField存入取出可能有差异
    涉及金钱等需要精确的用DecimalField
    
    DateField(auto_now_add = true)
####### 默认赋值为当前时间,记录创建时间   

    DateField(auto_now = true)
####### 默认赋值为当前时间,记录最后一次更新数据的时间,修改了此对象的任何数据都要更新时间    
    
两者不能同时使用  
    
TimeField DateTimeField参数同上

    
    


  
