#from django.conf.urls import url
from goods.views import IndexView, DetailView, ListView
from django.urls import path, re_path
urlpatterns = [
    #url(r'^index$', IndexView.as_view(), name='index'), # 首页
    re_path('index/', IndexView.as_view(), name='index'), # 首页
    #url(r'^goods/(?P<goods_id>\d+)$', DetailView.as_view(), name='detail'), # 详情页
    re_path('goods/(?P<goods_id>\d+)$', DetailView.as_view(), name='detail'), # 详情页
    #url(r'^list/(?P<type_id>\d+)/(?P<page>\d+)$', ListView.as_view(), name='list'), # 列表页
    re_path('list/(?P<type_id>\d+)/(?P<page>\d+)$', ListView.as_view(), name='list'), # 列表页
]
