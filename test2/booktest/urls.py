from django.conf.urls import url
from booktest import views

urlpatterns=[
    url(r'^$',views.index),#首页显示
    url(r'^delete(\d+)/$',views.delete),#删除
    url(r'^create/$',views.create),#创建
    url(r'^displayInfo(?P<pIndex>[0-9]*)$',views.displayInfo),#显示英雄信息，带分页
    url(r'^addhero$',views.addhero),#添加英雄保存数据
    url(r'^heroinfo$',views.heroinfo),#ajax处理返回图书数据
    url(r'^showaddhero$',views.showaddhero),#创建英雄页面
    url(r'^pic_upload$',views.pic_upload),#上传图片显示
    url(r'^pic_handle/$',views.pic_handle),#上传图片处理
    url(r'^pic_show$',views.pic_show),#显示图片
]
