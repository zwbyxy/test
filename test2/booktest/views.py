from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from booktest.models import *
from datetime import date
from django.conf import settings
from django.http import HttpResponse,JsonResponse
from django.core.paginator import Paginator

#查询所有图书并显示
def index(request):
    list=BookInfo.objects.all()
    return render(request,'booktest/index.html',{'list':list})

#创建新图书
def create(request):
    book=BookInfo()
    book.btitle = '流星蝴蝶剑'
    book.bpub_date = date(1995,12,30)
    book.save()
    #转向到首页
    return redirect('/')

#逻辑删除指定编号的图书
def delete(request,id):
    book=BookInfo.objects.get(id=int(id))
    book.delete()
    #转向到首页
    return redirect('/')

#显示英雄信息
def displayInfo(request,pIndex):
    hlist=HeroInfo.objects.all()
    #将地区信息按一页10条进行分页
    p = Paginator(hlist, 10)
    #如果当前没有传递页码信息，则认为是第一页，这样写是为了请求第一页时可以不写页码
    if pIndex == '':
        pIndex = 1
    #通过url匹配的参数都是字符串类型，转换成int类型
    pIndex = int(pIndex)
    #获取第pIndex页的数据
    list2 = p.page(pIndex)
    #获取所有的页码信息
    plist = p.page_range
    #将当前页码、当前页的数据、页码信息传递到模板中
    return render(request, 'booktest/bookheroinfo.html', {'hlist': list2, 'plist': plist, 'pIndex': pIndex})
    #return render(request,'booktest/bookheroinfo.html',{'hlist':hlist})

#显示增页面
def showaddhero(request):
    return render(request,'booktest/addhero.html')

#创建英雄
def addhero(request):
    hname=request.POST.get('hname')
    hgender=request.POST.get('hgender')
    hcomment=request.POST.get('hcomment')
    hbook_id=request.POST.get('hbook')
    h=HeroInfo()
    h.hname=hname
    h.hgender=hgender
    h.hcomment=hcomment
    h.hbook_id=hbook_id
    #print(hbook_id)
    h.save()
    return redirect('/displayInfo')

#显示增页面
def pic_upload(request):
    return render(request,'booktest/pic_upload.html')

#上传图片
def pic_handle(request):
    f1=request.FILES.get('pic')
    fname='%s/file/%s'%(settings.MEDIA_ROOT,f1.name)
    with open(fname,'wb') as pic:
        for c in f1.chunks():
            pic.write(c)
    # 4.在数据库中保存上传记录
    PicTest.objects.create(pic='file/%s'%f1.name)
    return HttpResponse('OK')

#显示图片
def pic_show(request):
    pic=PicTest.objects.get(pk=1)
    context={'pic':pic}
    return render(request,'booktest/pic_show.html',context)

#获取图书，并json返回
def heroinfo(request):
    blist=BookInfo.objects.all()
    list=[]
    for book in blist:
        list.append([book.id,book.btitle])
    print(f'{list}aa'%list)
    return JsonResponse({'list':list})
