from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.generic import View

# Create your views here.
# Python高级-全部（html版）
#/help/help01
class Help01View(View):
    def get(self, request):
        '''显示Python高级-全部（html版）页面'''
        # 使用模板
        return render(request, 'help/index.html')
