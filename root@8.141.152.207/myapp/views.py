from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # resp = render(request, 'myapp/index.html')
    resp = render(request, 'myapp/newindex.html')
    return resp


def guess(request):
    sentence = request.POST.get('sentence')
    dic = {}
    dic['res'] = "您的输入是："+str(sentence) + "\n猜测结果是:" + "请等待功能实现"
    # resp = render(request, 'myapp/index.html', dic)
    resp = render(request, 'myapp/newindex.html', dic)
    return resp
