from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
import markdown #给文章摘要富文本化
from django.utils.html import strip_tags #这个函数用来去html文本的html标签
# coding: utf-8
# Create your models here.
"""
 Django 要求模型必须继承 models.Model 类。
 Category 只需要一个简单的分类名 name 就可以了。
 CharField 指定了分类名 name 的数据类型，CharField 是字符型，
 CharField 的 max_length 参数指定其最大长度，超过这个长度的分类名就不能被存入数据库。
 当然 Django 还为我们提供了多种其它的数据类型，如日期时间类型 DateTimeField、整数类型 IntegerField 等等。
 Django 内置的全部类型可查看文档：
 https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types
 """
# python_2_unicode_compatible 装饰器用于兼容 Python2
@python_2_unicode_compatible
class Category(models.Model):    #分类表的ORM继承子MODEL
    name=models.CharField(max_length=100)    #列名name,类型字符，最大100，id列自动创建
    def __str__(self):
        return self.name
@python_2_unicode_compatible
class Tag(models.Model):   #标签表
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
@python_2_unicode_compatible
class Post(models.Model):   #文章表库
    title=models.CharField(max_length=70)  #标题


    body=models.TextField()       #正文
    created_time=models.DateTimeField()   #创建时间，类型为时间型
    modified_time=models.DateTimeField()  #修改时间

    excerpt=models.CharField(max_length=200,blank=True)  #blanck允许空值

    category=models.ForeignKey(Category)  #设置外键，一篇文章只有一个分类，而一个分类可以有多篇文章
    '''一篇文章对应一个分类，而一个分类
    下有多个文章，将外键设在多的一方'''
    tags=models.ManyToManyField(Tag,blank=True)  #多对多的关系，一片文章可以多个标签，一个标签也可以对应多篇文章

    author=models.ForeignKey(User)  #设置外键对应用户表，User是Django写好的数据表，导入，一对多的关系
    views=models.PositiveIntegerField(default=10) #设置阅读量，默认为10,增加阅读量的字段
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.id})
    #捕获pk,reverse即根据参数和视图函数反向查找出url，文章设置绝对地址。


    def __str__(self):
        return self.title
    def increase_views(self):
        self.views+=1                 #调用这个方法则views数量加1
        self.save(update_fields=['views'])  #只更新views字段到数据库

    def save(self,*args,**kwargs): #保存了save应有的样子
        if not self.excerpt:
            md=markdown.Markdown(extensions=['markdown.extensions.extra',
                                             'markdown.extensions.codehilite',])
            #现将markdown实例化，用于渲染摘要
            self.excerpt=strip_tags(md.convert(self.body))[:54]#将html文本的html标签去除，然后通过markdown渲染，取前52个字
        super(Post,self).save(*args,**kwargs) #调用父类的save方法

    class Meta:  # 定义models.Model的子类的源属性，注意大小写
        ordering = ['-created_time', 'title']  # 定义Post的源排序根据时间逆序,时间想通过比较标题