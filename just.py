import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lilong.settings")
django.setup()
def main():
    from blog.models import Post

    blog=Post.objects.all().filter(id=2)
    print(blog.only('author'))

if __name__=='__main__':
    main()