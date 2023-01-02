from django.shortcuts import render
from myapp import models
import math
page = 1
def news(request, pageindex=None):
    global page
    pagesize = 8
    newsall = models.NewsData.objects.all().order_by('-id')
    datasize = len(newsall)
    total_page =math.ceil(datasize/pagesize)
    if pageindex==None:
        page = 1
        news_units =models.NewsData.objects.all().order_by('-id')[:pagesize]
    else :
        page = int(pageindex)
        startpage = pagesize * (page-1)
        news_units = models.NewsData.objects.all().order_by('-id')[startpage:startpage+8]
    currentpage = page
    return render(request, "news.html", locals())

def detail(request, detail_id=None):
    unit = models.NewsData.objects.get(id=detail_id)
    category = unit.catego
    title = unit.title
    pubtime = unit.pubtime
    nickname = unit.nickname
    message = unit.message
    unit.press += 1
    unit.save()

    return render(request, "detail.html", locals())
def login(request):

    return render(request, "login.html", locals())


# Create your views here.
