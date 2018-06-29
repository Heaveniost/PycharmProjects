from django.contrib import admin
from .models import TypeInfo,GoodsInfo

# superuser 123 qq123456


class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','ttitle']


class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id','gtitle','gprice','gunit','gclick','gintroduce','ginventory','gcontent',]


admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(GoodsInfo,GoodsInfoAdmin)