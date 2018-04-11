# mxonline
## 配置环境python3.6

    diff-match-patch (20121119)
    Django (2.0.4)
    django-crispy-forms (1.7.2)
    django-formtools (2.1)
    django-import-export (1.0.0)
    django-ranged-response (0.2.0)
    django-simple-captcha (0.5.6)
    et-xmlfile (1.0.1)
    future (0.16.0)
    httplib2 (0.11.3)
    jdcal (1.3)
    odfpy (1.3.6)
    openpyxl (2.5.2)
    Pillow (5.1.0)
    pip (9.0.3)
    PyMySQL (0.8.0)
    pytz (2018.3)
    PyYAML (3.12)
    setuptools (39.0.1)
    six (1.11.0)
    tablib (0.12.1)
    unicodecsv (0.14.1)
    wheel (0.31.0)
    xlrd (1.1.0)
    xlwt (1.3.0)
##插件升级后的问题及解决
1. 连接数据库
    pip install pymsql  
    在mxonline/__init__.py中  
    import pymysql  
    pymysql.install_as_MySQLdb()
2. django2.0把from django.core.urlresolvers修改成了django.urls
3. django2.0中需要给外键ForeignKey指定on_delete参数
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
4. django2.0 forms表单初始化只需要一个参数
    报错  
    model = ModelChoiceField(label=_(u'Target Model'), widget=exwidgets.AdminSelectWidget)  
    File "D:\Envs\django-xadmin\lib\site-packages\xadmin-0.6.1-py3.6.egg\xadmin\views\dashboard.py", line 284, in __init__  
    forms.Field.__init__(self, required, widget, label, initial, help_text, *args, **kwargs)  
    TypeError: __init__() takes 1 positional argument but 6 were given  
    解决  
    forms.Field.__init__(self)  
5. 导入QUERY_TERMS报错
    把  
    from django.db.models.sql.query import LOOKUP_SEP, QUERY_TERMS  
    改为  
    from django.db.models.sql.query import LOOKUP_SEP  
    from django.db.models.sql.constants import QUERY_TERMS  
6. Settings缺少MIDDLEWARE_CLASSES属性，django2.0把MIDDLEWARE_ClASSES改成MIDDLEWARE
    把  
    if settings.LANGUAGES and 'django.middleware.locale.LocaleMiddleware' in settings.MIDDLEWARE_ClASSES:  
    改为  
    if settings.LANGUAGES and 'django.middleware.locale.LocaleMiddleware' in settings.MIDDLEWARE:
7. Django导入xadmin提示No module named import_export.admin
    pip install django-import-export 
