from ..models import Post,Category,Tag
from django import template
from django.db.models.aggregates import Count

register=template.Library()  #现在模板类中注册

'''最新文章标签'''
@register.simple_tag   #将下面的标签函数装饰为simple_tag，这样就可以在模板语法中调用{% get_recent_posts %}这个函数
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]
#取出所有文章按创建时间逆排序，取前五个

'''归档模板标签'''
@register.simple_tag
def archives():
    return Post.objects.dates('created_time','month',order='DESC')
#返回一个查询后的列表，且为date对象，第一个是post的创建时间，第二个参数是精确度月份，第三个是排列顺序，逆序.

'''分类模板标签'''
@register.simple_tag
def get_category():
    return Category.objects.all()


'''每个分类的数量'''
@register.simple_tag
def get_category():
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    #__gt__为对象 的大于属性,相当于给个Category新增了一栏counts属性，'post'是小写,他与跳转后index.html中的'post'个数有关

'''标签云'''
@register.simple_tag
def get_tag():
    return Tag.objects.all()



