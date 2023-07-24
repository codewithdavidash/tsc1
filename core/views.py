from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from .models import HTML, JS, PYTHON, Comment, Assignments
from .forms import *


@login_required
def index(request):
    html = HTML.objects.all()
    js = JS.objects.all()
    python = PYTHON.objects.all()
    a = Assignments.objects.all()[0:9]
    return render(request, 'core/index.html', {
        'html': html,
        'js': js,
        'python': python,
        'a': a
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {
        'form': form
    })

def login(request):
    form = LoginForm()
    return render(request, 'core/login.html', {
        'form': form
    })

@login_required
def myaccount(request):
    return render(request, 'core/myaccount.html', {})

@login_required
def changepassword(request):
    return render(request, 'core/changepassword.html', {})

def info(request):
    return render(request, 'core/info.html', {})

def terms_and_conditions(request):
    return render(request, 'core/terms_and_conditions.html', {})

@login_required
def add(request):
    return render(request, 'core/add.html', {
    })

@login_required
def add_html_videos(request):
    if request.method == 'POST':
        form = htmlForm(request.POST, request.FILES)
        if form.is_valid():
            new_data = form.save()
            new_data.save()
            return redirect('/')
    else:
        form = htmlForm()
    return render(request, 'core/add_html_videos.html', {
        'form': form
    })

@login_required
def add_js_videos(request):
    if request.method == 'POST':
        form = jsForm(request.POST, request.FILES)
        if form.is_valid():
            new_data = form.save()
            new_data.save()
            return redirect('/')
    else:
        form = jsForm()
    return render(request, 'core/add_js_videos.html', {
        'form': form
    })

@login_required
def add_python_videos(request):
    if request.method == 'POST':
        form = pythonForm(request.POST, request.FILES)
        if form.is_valid():
            new_data = form.save(commit=False)
            new_data.save()
            return redirect('/')
    else:
        form = pythonForm()
    return render(request, 'core/add_python_videos.html', {
        'form': form
    })

@login_required
def comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/comment/')
    else:
        form = CommentForm()
    comment = Comment.objects.all()
    return render(request, 'core/comment.html', {
    'comment': comment,
    'form': form
    })

@login_required
def submit_assignments(request):
    if request.method == 'POST':
        form = AssignmentsForm(request.POST, request.FILES)
        if form.is_valid():
            new_data = form.save(commit=False)
            new_data.save()
            messages.success(request, 'Your Assignment was submitted successfully')
            return redirect('/')
    else:
        form = AssignmentsForm()
    
    return render(request, 'core/submit_assignments.html', {
        'form': form
    })