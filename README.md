# Django
Django学习

## Test  
Markdown  

    注意点1:  
    配置网站地址 统一加 /  
    
    ###/creat
    这种网址是: 域名 + 路径
    
    ### create
    这种是 当前页面的路径 拼接 creat,当出现 / 的时候 会出问题
    
    urls.py配置 末尾统一加 '/' 
    html中 地址开头统一用 '/create'这样的就行了
    一头一尾