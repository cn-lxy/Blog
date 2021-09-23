from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


# 叮叮书店
def DingBookStore(request):
    return render(request, 'blog-dingDing-index.html')


# 联系我们
def contactUs(request):
    return render(request, '联系我们.html')


# 购物车
def shopping(request):
    return render(request, '购物车.html')


