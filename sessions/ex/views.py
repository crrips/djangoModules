from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from random import choice
from sessions.settings import NAMES
from .forms import RegisterForm, LoginForm, TipForm
from .models import Site_User, Tip
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required


@login_required
def votes(request):
    if request.method == 'POST' and 'upvote_tip' in request.POST:
        tip = get_object_or_404(Tip, pk=request.POST['upvote_tip'])
        if request.user in tip.upvoters.all():
            tip.upvoters.remove(request.user)
            tip.upvotes -= 1
        else:
            if request.user in tip.downvoters.all():
                tip.downvoters.remove(request.user)
                tip.downvotes -= 1
            tip.upvoters.add(request.user)
            tip.upvotes += 1
        tip.save()
        return redirect('home')
    
    if request.method == 'POST' and 'downvote_tip' in request.POST:
        tip = get_object_or_404(Tip, pk=request.POST['downvote_tip'])
        if request.user in tip.downvoters.all():
            tip.downvoters.remove(request.user)
            tip.downvotes -= 1
        else:
            if request.user == get_object_or_404(Tip, pk=request.POST['downvote_tip']).author or request.user.has_perm('ex.downvote_tip') or request.user.reputation >= 15:
                if request.user in tip.upvoters.all():
                    tip.upvoters.remove(request.user)
                    tip.upvotes -= 1
                tip.downvoters.add(request.user)
                tip.downvotes += 1
        tip.save()
        return redirect('home')
    
    if request.method == 'POST' and 'delete_tip' in request.POST:
        if request.user == get_object_or_404(Tip, pk=request.POST['delete_tip']).author or request.user.has_perm('ex.delete_tip') or request.user.reputation >= 30:
            tip = get_object_or_404(Tip, pk=request.POST['delete_tip'])
            tip.delete()
            return redirect('home')


def home(request):
    name = ''
    new_tip_status = False
    new_tip = None
    
    if request.method == 'POST' and 'logout' in request.POST:
        logout(request)
        return redirect('home')
    if request.method == 'POST' and 'new_tip' in request.POST:
        new_tip_status = True
        new_tip = TipForm()
    if request.method == 'POST' and 'cancel_tip' in request.POST:
        new_tip_status = False
        new_tip = None
        return redirect('home')
    if request.method == 'POST' and 'create_tip' in request.POST:
        new_tip = TipForm(request.POST)
        if new_tip.is_valid():
            tip = Tip(content=new_tip.cleaned_data['content'], author=request.user)
            tip.save()
            new_tip_status = False
            new_tip = None
            return redirect('home')
    votes(request)
        
    tips = Tip.objects.all().order_by('-date')
    user = None
    if request.user.is_authenticated:
        user = request.user
        user.reputation = user.upvoters.count() * 5 - user.downvoters.count() * 2
        user.save()
    else:
        name = choice(NAMES)
    response = render(request, 'ex/home.html', {'name': name, 'user': user, 'new_tip_status': new_tip_status, 'new_tip': new_tip, 'tips': tips})
    return response


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] != form.cleaned_data['password_confirm']:
                response = render(request, 'ex/register.html', {'form': form, 'error': "Passwords don't match"})
                return response
            if form.cleaned_data['username'] in Site_User.objects.values_list('username', flat=True):
                response = render(request, 'ex/register.html', {'form': form, 'error': 'User already registered'})
                return response
            user = Site_User(username=form.cleaned_data['username'])
            user.set_password(form.cleaned_data['password'])
            user.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            auth_login(request, user)
        response = redirect('home')
        return response
    response = render(request, 'ex/register.html', {'form': RegisterForm()})
    return response


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['username'] not in Site_User.objects.values_list('username', flat=True):
                response = render(request, 'ex/login.html', {'form': form, 'error': 'User not registered'})
                return response
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                auth_login(request, user)
                response = redirect('home')
                return response
            else:
                response = render(request, 'ex/login.html', {'form': form, 'error': 'Incorrect password'})
                return response
    response = render(request, 'ex/login.html', {'form': LoginForm()})
    return response

