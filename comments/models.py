from django.db import models
from django.utils.six import python_2_unicode_compatible#用于兼容Python2

# Create your models here.
@python_2_unicode_compatible
class Comment(models.Model):
    name=models.CharField(max_length=100)  #名字，字符型
    email=models.EmailField(max_length=255)  #用于存储Email的类型
    url=models.URLField(blank=True)      #存储URL地址
    text=models.TextField()
    created_time=models.DateTimeField(auto_now_add=True) #时间，自动添加修改时间
    post=models.ForeignKey('blog.Post')  #外键和blog数据库模板的Post类，连接,一篇文章可有多个评论
    #而一条评论只对应一片文章下

    def __str__(self):
        return self.text[:20]
