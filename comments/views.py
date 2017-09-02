from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
import markdown
from .models import Comment
from .forms import CommentForm

# Create your views here.

def post_comment(request,post_pk):
    '''先获取被评论的文章，因为后面需要评论与被评论的文章关联起来
        这里使用快捷函数get_object_or_404
        这个函数的作用是当获取的文章（post）存在是返回，否则返回404给用户
    '''
    post=get_object_or_404(Post,pk=post_pk)

    if request.method=='POST':
        #当请求是POST方式是才出力

        form=CommentForm(request.POST)
        #用户提交的参数数据存在request.POST当中，是个类字典的对象
        #利用数据结合构造CommentForm表单的实例

        if form.is_valid():#is_valid方法检查表单数据是否合法
            #合法调用表单的save方法存入数据库
            comment=form.save(commit=False)
            #commit=False的作用是仅仅利用form的内容生成comment的实例，还未提交到数据库

            comment.post=post #将评论和被评论的文章关联
            comment.save()   #将评论保存到Comment数据库

            return redirect(post)
            #重新定向到post的详情页，实际当redirect函数接受到一个模型的实例时，他会调用这个模型的get_absolute_url方法
            #然后这个方法返回post的URL，重定向到这个URL
        else:
            #检测到数据不合法时，重新渲染详情页，并且渲染表单的错误
            #因此传了三个模板变量给detail.html
            #一个是文章（post），一个是评论列表，一个是表单form
            #这里用到post.comment_set.all()方法
            #这个方法类似Post.objects.all()
            #作用是获取该文章下的全部评论
            #因为Post和Comment是外键关联的
            #因此使用Post.comment_set.all()可以反向查询一篇文章的全部评论
            comment_list=post.comment_set.all()
            context={'post':post,
                     'form':form,
                     'comment_list':comment_list
            }
            return render(request,'blog/detail.html',context=context)
    return redirect(post)  #如果不是post请求，那么重转到post页，即文章详情页
#redirect接受url参数，或者模型实例，但该实例必须实现了get_absolute_url的方法才能重定向。
#Post.comment_set.all()等价于：Comment.objects.all().filter(post=post)即一篇文章下的所有评论。




