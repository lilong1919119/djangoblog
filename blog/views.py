from django.shortcuts import render, get_object_or_404
import markdown
from django.http import HttpResponse
from .models import Post,Category,Tag
from comments.forms import CommentForm
# Create your views here.

'''get_object_or_404作用，注意这里我们用到了从 django.shortcuts 模块导入的 get_object_or_404 
方法，其作用就是当传入的 pk 对应的 Post 在数据库存在时，就返回对应的 post，如果不存在，就
给用户返回一个 404 错误，表明用户请求的文章不存在。'''
def index(request):
    # return HttpResponse('欢迎访问我的首页')    不加渲染直接利用response返回字符串
    post_list=Post.objects.all()
    return render(request,'blog/index.html',context={'post_list':post_list})
#render函数构造httpresponse,第一个是传入请求后，第二个为渲染的模板路径，第三个为模板内变量赋值

def detail(request,pk):  #从<pk>中拿到的值
    post=get_object_or_404(Post,id=pk )
    post.increase_views()  #当浏览时，views属性加1
    post.body=markdown.markdown(post.body, extensions=[
                                      'markdown.extensions.extra',  #拓展，如表格等
                                      'markdown.extensions.codehilite',  #拓展代码高亮
                                      'markdown.extensions.toc',    #
                                  ])  #注入markdown,使文章实体更充实

    form = CommentForm()  #将评论实例
    comment_list = post.comment_set.all().order_by('-created_time')  # 获取这篇文章下的所有评论,这两句是作用给评论
    context = {'post':post,'form':form,'comment_list':comment_list,}
    return render(request,'blog/detail.html',context=context)

def archives(request,year,month):
    post_list=Post.objects.all().filter(created_time__year=year,created_time__month=month).order_by('-created_time')
    #filter相当于where,查询项
    return render(request,'blog/index.html',context={'post_list':post_list})

def category(request,pk):
    cate=get_object_or_404(Category,pk=pk)
    post_list=Post.objects.all().filter(category=cate).order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})

def tag(request,pk):
    tg=get_object_or_404(Tag,pk=pk)
    post_list=Post.objects.filter(tags=tg).order_by('-created_time')
    return render(request,'blog/index.html',context={'post-list':post_list})


