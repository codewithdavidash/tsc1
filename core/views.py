from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm
from django.db.models import Q
from .models import (
    HTML_CSS,
    JavaScript,
    Python
)


@login_required
def index(request):
    html_css = HTML_CSS.objects.all()[0:6]
    js = JavaScript.objects.all()[0:6]
    py = Python.objects.all()[0:6]
    context = {
        'html_css': html_css,
        'js': js,
        'py': py,
    }
    return render(request, 'core/index.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created for '+ user)
            return redirect('/login/')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'core/register.html', context)

@login_required
def search(request):
    query = request.GET.get('query', '')
    html_css = HTML_CSS.objects.all()
    js = JavaScript.objects.all()
    py = Python.objects.all()
    if query:
        html_css = html_css.filter(Q(title__icontains=query) | Q(description__icontains=query))
        js = js.filter(Q(title__icontains=query) | Q(description__icontains=query))
        py = py.filter(Q(title__icontains=query) | Q(description__icontains=query))
    context = {
        'query': query,
        'html_css': html_css,
        'js': js,
        'py': py,
    }
    return render(request, 'core/search.html', context)

@login_required
def menu(request):
    context = {}
    return render(request, 'core/menu.html', context)

@login_required
def delete_accounts(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'core/delete_accounts.html', context)

@login_required
def user_accounts(request, id):
    users = User.objects.get(id=id)
    if request.method == 'POST':
        users.delete()
        return redirect('/delete_accounts/')
    context = {
        'users': users
    }
    return render(request, 'core/user_accounts.html', context)

def terms_and_conditions(request):
    context = {}
    return render(request, 'core/terms_and_conditions.html', context)