from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from myapp import models
import math
page = 1
def news(request,pageindex=None):
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
    messages = ''  # 初始時清除訊息
    if request.method == 'POST':  # 如果是以POST方式才處理
        name = request.POST['username'].strip()  # 取得輸入帳號
        password = request.POST['password']  # 取得輸入密碼
        user1 = authenticate(username=name, password=password)  # 驗證
        if user1 is not None:  # 驗證通過
            messages = '登入失敗！'
            if user1.is_active:  # 帳號有效
                auth.login(request, user1)  # 登入
                return redirect('/adminmain/')  # 開啟管理頁面
            else:  # 帳號無效
                messages = '帳號尚未啟用！'
        else:  # 驗證未通過
            messages = '帳號密碼錯誤！'
    return render(request, "login.html", locals())

def adminmain(request,pageindex=None):
    global page
    pagesize = 8
    newsall = models.NewsData.objects.all().order_by('-id')
    datasize = len(newsall)
    total_page = math.ceil(datasize / pagesize)
    if pageindex == None:
        page = 1
        news_units = models.NewsData.objects.all().order_by('-id')[:pagesize]
    else:
        page = int(pageindex)
        startpage = pagesize * (page - 1)
        news_units = models.NewsData.objects.all().order_by('-id')[startpage:startpage + 8]
    currentpage = page

    return render(request, "adminmain.html", locals())

def admin_add(request):
    message = ''  # 清除訊息
    category = request.POST.get('news_type', '')  # 取得輸入的類別
    subject = request.POST.get('news_subject', '')
    editor = request.POST.get('news_editor', '')
    content = request.POST.get('news_content', '')
    ok = request.POST.get('news_ok', '')
    if subject == '' or editor == '' or content == '':  # 若有欄位未填就顯示訊息
        message = '每一個欄位都要填寫...'
    else:
        if ok == 'yes':  # 根據ok值設定enabled欄位
            enabled = True
        else:
            enabled = False
        unit = models.NewsData.objects.create(catego=category, nickname=editor, title=subject, message=content,
                                              enabled=enabled, press=0)
        unit.save()
        return redirect('/adminmain/')
    return render(request, "admin_add.html", locals())
def admin_edit(request, newsid=None, edittype=None):  #修改資料
	unit = models.NewsData.objects.get(id=newsid)  #讀取指定資料
	categories = ["公告", "焦點","運動","社會", "氣象", "活動" ,"其他"]
	if edittype == None:  #進入修改頁面,顯示原有資料
		type = unit.catego
		subject = unit.title
		editor = unit.nickname
		content = unit.message
		ok = unit.enabled
	elif edittype == '1':  #修改完畢,存檔
		category = request.POST.get('news_type', '')
		subject = request.POST.get('news_subject', '')
		editor = request.POST.get('news_editor', '')
		content = request.POST.get('news_content', '')
		ok = request.POST.get('news_ok', '')
		if ok=='yes':
			enabled = True
		else:
			enabled = False
		unit.catego=category
		unit.nickname=editor
		unit.title=subject
		unit.message=content
		unit.enabled=enabled
		unit.save()
		return redirect('/adminmain/')
	return render(request, "admin_edit.html", locals())

def admin_delete(request, newsid=None, deletetype=None):  #刪除資料
	unit = models.NewsData.objects.get(id=newsid)  #讀取指定資料
	if deletetype == None:  #進入刪除頁面,顯示原有資料
		type = str(unit.catego.strip())
		subject = unit.title
		editor = unit.nickname
		content = unit.message
		date = unit.pubtime
	elif deletetype == '1':  #按刪除鈕
		unit.delete()
		return redirect('/adminmain/')
	return render(request, "admin_delete.html", locals())


# Create your views here.
