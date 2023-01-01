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
        news_units =models.NewsData.objects.all().order_by('-pubtime')[:pagesize]
    else :
        page = int(pageindex)
        startpage = pagesize * (page-1)
        news_units = models.NewsData.objects.all().order_by('-pubtime')[startpage:startpage+8]
    currentpage = page
    return render(request, "news.html", locals())


# Create your views here.
