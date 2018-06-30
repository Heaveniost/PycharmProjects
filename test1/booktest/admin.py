#conding=utf-8
from django.contrib import admin
from .models import *


class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 2


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['pk','btitle','bpub_date',] #页面上的显示
    #display 拼写错了 导致BookInfoAdmin 又不报错
    list_filter = ['btitle']
    search_fields=['btitle']
    list_per_page=10
    #fields=['bpub_date','btitle'] #进去后显示的顺序
    fieldsets=[
        ('basic',{'fields':['btitle',]}),
        ('super',{'fields':['bpub_date',]}),
    ]
    #fields fieldsets 两者不能同时存在
    inlines = [HeroInfoInline]
    #实现关联注册


def gender(self):
    if self.hgender:
        return '男'
    else:
        return '女'
gender.short_description='性别'

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','hname','hgender','hcontent']


admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)