from django.contrib import admin
from .models import Post,Category,Tag
# Register your models here.
'''自定义的admin'''
class Postadmin(admin.ModelAdmin):
    list_display = ['title','created_time','modified_time','author']

admin.site.register(Post,Postadmin)
admin.site.register(Category)
admin.site.register(Tag)

