from django.shortcuts import render, get_object_or_404, redirect
from .models import Home
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .forms import HomeUpdate
# Create your views here.

def home(request):
    homes = Home.objects
    home_list = Home.objects.all()
    paginator = Paginator(home_list, 10)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'home.html', {'homes':homes, 'articles':articles})

def detail(request, home_id):
    home_detail = get_object_or_404(Home, pk=home_id)
    return render(request, 'detail.html', {'home': home_detail})

def new(request):
    if request.user.is_authenticated:
        #login 한 상태라면 new 포스트 html로 보내기.
        return render(request, 'new.html')
    else:
        #회원정보가 존재하지 않는다면, 에러인자와 함께 home 템플릿으로 돌아가기.
        homes = Home.objects
        home_list = Home.objects.all()
        paginator = Paginator(home_list, 10)
        page = request.GET.get('page')
        articles = paginator.get_page(page)
        return render(request, 'report.html', {'homes':homes, 'articles':articles, 'error': 'You have to login to make newpost'})

def new_g(request):
    if request.user.is_authenticated:
        #login 한 상태라면 new 포스트 html로 보내기.
        return render(request, 'new_g.html')
    else:
        #회원정보가 존재하지 않는다면, 에러인자와 함께 home 템플릿으로 돌아가기.
        homes = Home.objects
        home_list = Home.objects.all()
        paginator = Paginator(home_list, 10)
        page = request.GET.get('page')
        articles = paginator.get_page(page)
        return render(request, 'report_g.html', {'homes':homes, 'articles':articles, 'error': 'You have to login to make newpost'})

def create(request):
    home = Home()
    home.author = request.user
    home.use = "동아리"
    home.clubname = request.GET['clubname']
    home.kakaoid = request.GET['kakaoid']
    home.phonenumber = request.GET['phonenumber']
    home.title = request.GET['title']
    home.body = request.GET['body']
    home.pub_date = timezone.datetime.now()
    home.save()
    return redirect('/home/' + str(home.id) + '/reportDetail/')

def create_g(request):
    home = Home()
    home.author = request.user
    home.use = "동아리"
    home.clubname = request.GET['clubname']
    home.kakaoid = request.GET['kakaoid']
    home.phonenumber = request.GET['phonenumber']
    home.title = request.GET['title']
    home.body = request.GET['body']
    home.pub_date = timezone.datetime.now()
    home.save()
    return redirect('/home/' + str(home.id) + '/reportDetail_g/')

def delete(request, home_id):
    Home.objects.get(id=home_id).delete()
    return redirect('/home/report/')

def delete_a(request, home_id):
    Home.objects.get(id=home_id).delete()
    return redirect('/home/ad/')

def delete_s(request, home_id):
    Home.objects.get(id=home_id).delete()
    return redirect('/home/spec/')

def delete_r(request, home_id):
    Home.objects.get(id=home_id).delete()
    return redirect('/home/revise/')

def update_c(request, home_id):
    home = Home.objects.get(id=home_id)

    if request.method =='POST':
        form = HomeUpdate(request.POST)
        if form.is_valid():
            home.title = form.cleaned_data['title']
            home.body = form.cleaned_data['body']
            home.kakaoid = form.cleaned_data['kakaoid']
            home.phonenumber = form.cleaned_data['phonenumber']
            home.pub_date=timezone.now()
            home.save()
            return redirect('/home/' + str(home.id) + '/reportDetail/') #여기가 문제...
    else:
        form = HomeUpdate(instance = home)
 
        return render(request,'update.html', {'form':form})

def update_r(request, home_id):
    home = Home.objects.get(id=home_id)

    if request.method =='POST':
        form = HomeUpdate(request.POST)
        if form.is_valid():
            home.title = form.cleaned_data['title']
            home.body = form.cleaned_data['body']
            home.kakaoid = form.cleaned_data['kakaoid']
            home.phonenumber = form.cleaned_data['phonenumber']
            home.pub_date=timezone.now()
            home.save()
            return redirect('/home/revise/')
    else:
        form = HomeUpdate(instance = home)
 
        return render(request,'update.html', {'form':form})

def update_a(request, home_id):
    home = Home.objects.get(id=home_id)

    if request.method =='POST':
        form = HomeUpdate(request.POST)
        if form.is_valid():
            home.title = form.cleaned_data['title']
            home.body = form.cleaned_data['body']
            home.kakaoid = form.cleaned_data['kakaoid']
            home.phonenumber = form.cleaned_data['phonenumber']
            home.pub_date=timezone.now()
            home.save()
            return redirect('/home/' + str(home.id) + '/adDetail/')
    else:
        form = HomeUpdate(instance = home)
 
        return render(request,'update.html', {'form':form})

def update_s(request, home_id):
    home = Home.objects.get(id=home_id)

    if request.method =='POST':
        form = HomeUpdate(request.POST)
        if form.is_valid():
            home.title = form.cleaned_data['title']
            home.body = form.cleaned_data['body']
            home.kakaoid = form.cleaned_data['kakaoid']
            home.phonenumber = form.cleaned_data['phonenumber']
            home.pub_date=timezone.now()
            home.save()
            return redirect('/home/' + str(home.id) + '/specDetail/')
    else:
        form = HomeUpdate(instance = home)
 
        return render(request,'update.html', {'form':form})

def revise(request):
    homes = Home.objects
    return render(request, 'revise.html', {'homes':homes})

def report(request):
    homes = Home.objects
    home_list = Home.objects.all()
    paginator = Paginator(home_list, 10)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'report.html', {'homes':homes, 'articles':articles})

def report_g(request):
    homes = Home.objects
    home_list = Home.objects.all()
    paginator = Paginator(home_list, 10)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'report_g.html', {'homes':homes, 'articles':articles})

def reportDetail(request, home_id):
    home_detail = get_object_or_404(Home, pk=home_id)
    return render(request, 'reportDetail.html', {'home': home_detail})

def reportDetail_g(request, home_id):
    home_detail = get_object_or_404(Home, pk=home_id)
    return render(request, 'reportDetail_g.html', {'home': home_detail})

def ad(request):
    homes = Home.objects
    home_list = Home.objects.all()
    paginator = Paginator(home_list, 10)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'ad.html', {'homes':homes, 'articles':articles})

def adDetail(request, home_id):
    home_detail = get_object_or_404(Home, pk=home_id)
    return render(request, 'adDetail.html', {'home': home_detail})

def spec(request):
    homes = Home.objects
    home_list = Home.objects.all()
    paginator = Paginator(home_list, 10)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'spec.html', {'homes':homes, 'articles':articles})

def spec_l(request):
    homes = Home.objects
    home_list = Home.objects.all()
    paginator = Paginator(home_list, 10)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'spec_l.html', {'homes':homes, 'articles':articles})

def specDetail(request, home_id):
    home_detail = get_object_or_404(Home, pk=home_id)
    return render(request, 'specDetail.html', {'home': home_detail})

def specDetail_l(request, home_id):
    home_detail = get_object_or_404(Home, pk=home_id)
    return render(request, 'specDetail_l.html', {'home': home_detail})

def newSpec(request):
    if request.user.is_authenticated:
        #login 한 상태라면 new 포스트 html로 보내기.
        return render(request, 'newSpec.html')
    else:
        #회원정보가 존재하지 않는다면, 에러인자와 함께 home 템플릿으로 돌아가기.
        homes = Home.objects
        home_list = Home.objects.all()
        paginator = Paginator(home_list, 10)
        page = request.GET.get('page')
        articles = paginator.get_page(page)
        return render(request, 'spec.html', {'homes':homes, 'articles':articles, 'error': 'You have to login to make newpost'})

def newSpec_l(request):
    if request.user.is_authenticated:
        #login 한 상태라면 new 포스트 html로 보내기.
        return render(request, 'newSpec_l.html')
    else:
        #회원정보가 존재하지 않는다면, 에러인자와 함께 home 템플릿으로 돌아가기.
        homes = Home.objects
        home_list = Home.objects.all()
        paginator = Paginator(home_list, 10)
        page = request.GET.get('page')
        articles = paginator.get_page(page)
        return render(request, 'spec_l.html', {'homes':homes, 'articles':articles, 'error': 'You have to login to make newpost'})


def newAd(request):
    if request.user.is_authenticated:
        #login 한 상태라면 new 포스트 html로 보내기.
        return render(request, 'newAd.html')
    else:
        #회원정보가 존재하지 않는다면, 에러인자와 함께 home 템플릿으로 돌아가기.
        homes = Home.objects
        home_list = Home.objects.all()
        paginator = Paginator(home_list, 10)
        page = request.GET.get('page')
        articles = paginator.get_page(page)
        return render(request, 'ad.html', {'homes':homes, 'articles':articles, 'error': 'You have to login to make newpost'})

def createSpec(request):
    home = Home()
    home.author = request.user
    home.use = "대외활동"
    home.clubname = request.GET['clubname']
    home.kakaoid = request.GET['kakaoid']
    home.phonenumber = request.GET['phonenumber']
    home.title = request.GET['title']
    home.body = request.GET['body']
    home.pub_date = timezone.datetime.now()
    home.save()
    return redirect('/home/' + str(home.id) + '/specDetail/')


def createSpec_l(request):
    home = Home()
    home.author = request.user
    home.use = "대외활동"
    home.clubname = request.GET['clubname']
    home.kakaoid = request.GET['kakaoid']
    home.phonenumber = request.GET['phonenumber']
    home.title = request.GET['title']
    home.body = request.GET['body']
    home.pub_date = timezone.datetime.now()
    home.save()
    return redirect('/home/' + str(home.id) + '/specDetail_l/')

def newAd(request):
    if request.user.is_authenticated:
        #login 한 상태라면 new 포스트 html로 보내기.
        return render(request, 'newAd.html')
    else:
        #회원정보가 존재하지 않는다면, 에러인자와 함께 home 템플릿으로 돌아가기.
        homes = Home.objects
        home_list = Home.objects.all()
        paginator = Paginator(home_list, 10)
        page = request.GET.get('page')
        articles = paginator.get_page(page)
        return render(request, 'ad.html', {'homes':homes, 'articles':articles, 'error': 'You have to login to make newpost'})


def createAd(request):
    home = Home()
    home.author = request.user
    home.use = "홍보"
    home.clubname = request.GET['clubname']
    home.kakaoid = request.GET['kakaoid']
    home.phonenumber = request.GET['phonenumber']
    home.title = request.GET['title']
    home.body = request.GET['body']
    home.pub_date = timezone.datetime.now()
    home.save()
    return redirect('/home/' + str(home.id) + '/adDetail/')

def update(request, home_id):
    home = Home.objects.get(id=home_id)

    if request.method =='POST':
        form = HomeUpdate(request.POST)
        if form.is_valid():
            home.title = form.cleaned_data['title']
            home.body = form.cleaned_data['body']
            home.pub_date=timezone.now()
            home.save()
            return redirect('/home/' + str(home.id))
    else:
        form = HomeUpdate(instance = home)
 
        return render(request,'update.html', {'form':form})
