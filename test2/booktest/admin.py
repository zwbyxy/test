from django.contrib import admin

# Register your models here.
from booktest.models import *

class AreaTabularInline(admin.TabularInline):
    model = AreaInfo#关联子对象
    extra = 2#额外编辑2个子对象

class AreaAdmin(admin.ModelAdmin):
    list_per_page = 10 #每页中显示多少条数据
    actions_on_bottom=True
    actions_on_top=False
    list_display = ['id','atitle','title','parent']
    search_fields=['atitle']
    fieldsets = (
        ('基本', {'fields': ['atitle']}),
        ('高级', {'fields': ['aParent']})
    )
    inlines = [AreaTabularInline]

    

admin.site.register(AreaInfo,AreaAdmin)
admin.site.register(PicTest)
