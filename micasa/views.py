from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404
from .models import *
from django.contrib import messages
from . forms import *
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    hoods = Hood.objects.all()
    return render(request,'home.html',locals())


@login_required(login_url='/accounts/login/')
def upload_hood(request):
    current_user = request.user
    if request.method == 'POST':
        form = HoodForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            hood.owner= current_user
            upload.save()
            return redirect('home')
    else:
        form = HoodForm()
    return render(request, 'upload_hood.html', locals())


@login_required(login_url='/accounts/login/')
def hood(request,hood_id):
    current_user = request.user
    hood_name = current_user.profile.hood
    hood = Hood.objects.get(id=request.user.profile.hood.id)
    businesses = Business.get_business(hood_id)
    posts = Post.get_post(hood_id)

    return render(request,'hood.html',locals())


@login_required(login_url='/accounts/login')
def join(request,hood_id):
    hood = Hood.objects.get(id=hood_id)
    current_user = request.user
    current_user.profile.hood = hood
    current_user.profile.save()
    return redirect('hood',hood_id)


@login_required(login_url='/accounts/login')
def leave(request,hood_id):
    current_user = request.user
    current_user.profile.hood = None
    current_user.profile.save()
    return redirect('home')