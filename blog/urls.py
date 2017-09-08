from django.conf.urls import url
from . import views
'''绑定url'''
app_name='blog'   #是指这个urls.py模块属于blog,命名空间
urlpatterns=[url(r'^$',views.index,name='index'),#第一个参数是网址，第二个是处理函数，第三个给为处理函数index取得别名
            url(r'^post/(?P<pk>[0-9]+)/$',views.detail,name='detail'),#<pk>相当于blog:detail的pk值,放入model中的反查询
            url(r'^archive/(?P<year>[0-9]{4})/(?P<month>[1-9]|[1][0-2])$',views.archives,name='archives'),
             url(r'^category/(?P<pk>[0-9]+)$',views.category,name='category'),
             url(r'^tag/(?P<pk>[0-9]+)$',views.tag,name='tag'),
             ]
