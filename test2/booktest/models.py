from django.db import models

# Create your models here.

#定义图书模型类BookInfo
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)#图书名称
    bpub_date = models.DateField()#发布日期
    bread = models.IntegerField(default=0)#阅读量
    bcomment = models.IntegerField(default=0)#评论量
    isDelete = models.BooleanField(default=False)#逻辑删除

#定义英雄模型类HeroInfo
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)#英雄姓名
    hgender = models.BooleanField(default=True)#英雄性别
    isDelete = models.BooleanField(default=False)#逻辑删除
    hcomment = models.CharField(max_length=200)#英雄描述信息
    hbook = models.ForeignKey('BookInfo')#英雄与图书表的关系为一对多，所以属性定义在英雄模型类中

#定义地区模型类，存储省、市、区县信息
class AreaInfo(models.Model):
    atitle=models.CharField(verbose_name='区域名称(字段)',max_length=30)#名称
    aParent=models.ForeignKey('self',null=True,blank=True)#父级

    def title(self):
        return self.atitle
    title.admin_order_field='atitle'
    title.short_description='区域名称'

    def parent(self):
        if self.aParent is None:
          return ''
        return self.aParent.atitle
    parent.admin_order_field='atitle'
    parent.short_description='父级区域名称'
    def __str__(self):
        return self.atitle

#创建图片存储表
class PicTest(models.Model):
    pic = models.ImageField(upload_to='file/')
