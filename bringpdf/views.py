from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from django.shortcuts import HttpResponse,redirect
from bringpdf import models
from .models import Category,Banner,Pdf,Tags
def orm(request):
    pass


def global_variable(request):
    allcategory = Category.objects.all()
    remen = Pdf.objects.filter(tui__id=2)[:6]
    tags = Tags.objects.all()
    return locals()

def index(request):
    banner = Banner.objects.filter(is_active=True)[0:4]
    tui = Pdf.objects.filter(tui__id=1)[:3]
    allarticle = Pdf.objects.all().order_by('-id')[0:10]
    hot = Pdf.objects.all().order_by('views')[:10]

    return render(request,'index.html',locals())


#列表页
def list(request,lid):
    list = Pdf.objects.filter(category_id=lid)#获取通过URL传进来的lid，然后筛选出对应文章
    cname = Category.objects.get(id=lid)#获取当前文章的栏目名
    page = request.GET.get('page')  # 在URL中获取当前页面数
    paginator = Paginator(list, 5)  # 对查询到的数据对象list进行分页，设置超过5条数据就分页
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'list.html', locals())

#内容页
def show(request,sid):
    show = Pdf.objects.get(id=sid)#查询指定ID的文章
    hot = Pdf.objects.all().order_by('?')[:10]#内容下面的您可能感兴趣的文章，随机推荐
    previous_blog = Pdf.objects.filter(created_time__gt=show.created_time,category=show.category.id).first()
    netx_blog = Pdf.objects.filter(created_time__lt=show.created_time,category=show.category.id).last()
    show.views = show.views + 1
    show.save()
    return render(request, 'show.html', locals())

#标签页
def tag(request, tag):
    list = Pdf.objects.filter(tags__name=tag)#通过文章标签进行查询文章
    tname = Tags.objects.get(name=tag)#获取当前搜索的标签名
    page = request.GET.get('page')
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'tags.html', locals())


# 搜索页
def search(request):
    ss=request.GET.get('search')#获取搜索的关键词
    list = Pdf.objects.filter(name__icontains=ss)#获取到搜索关键词通过标题进行匹配
    page = request.GET.get('page')
    paginator = Paginator(list, 10)
    try:
        list = paginator.page(page) # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1) # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages) # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'search.html', locals())
# 关于我们
def about(request):
    allcategory = Category.objects.all()
    return render(request, 'page.html',locals())