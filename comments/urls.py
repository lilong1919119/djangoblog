from django.conf.urls import url
from . import views

app_name='comments'   #给这个app绑定名字，命名空间

urlpatterns=[url(r'^comment/post/(?P<post_pk>[0-9]+)$',views.post_comment,name='post_comment'),]
