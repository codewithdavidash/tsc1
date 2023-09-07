from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import *
from crud.forms import *

@login_required
def add(request):
    return render(request, 'crud/add.html')

# Create
@login_required
def create_html_css(request):
    if request.method == 'POST':
        form = html_css_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = html_css_form()
    context = {
        'form': form,
    }
    return render(request, 'crud/html_css.html', context)

# Create
@login_required
def create_js(request):
    if request.method == 'POST':
        form = js_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = js_form()
    context = {
        'form': form,
    }
    return render(request, 'crud/js.html', context)

# Create
@login_required
def create_py(request):
    if request.method == 'POST':
        form = py_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = py_form()
    context = {
        'form': form,
    }
    return render(request, 'crud/py.html', context)


# Update
@login_required
def update_html_css(request, id):
    html_css = HTML_CSS.objects.get(id=id)
    form = html_css_form(request.POST or None, instance=html_css)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = html_css_form(instance=html_css)
    context = {
        'form': form,
        'html_css': html_css
    }
    return render(request, 'crud/update_html_css.html', context)

# Update
@login_required
def update_js(request, id):
    js = JavaScript.objects.get(id=id)
    form = js_form(request.POST or None, instance=js)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = js_form(instance=js)
    context = {
        'form': form,
        'js': js
    }
    return render(request, 'crud/update_js.html', context)

# Update
@login_required
def update_py(request, id):
    py = Python.objects.get(id=id)
    form = py_form(request.POST or None, instance=py)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = py_form(instance=py)
    context = {
        'form': form,
        'py': py
    }
    return render(request, 'crud/update_py.html', context)

# delete
@login_required
def delete_html_css(request, id):
    html_css = HTML_CSS.objects.get(id=id)
    if request.method == 'POST':
        html_css.delete()
        return redirect('/')
    context = {
        'html_css': html_css
    }
    return render(request, 'crud/delete_html_css.html', context)

# delete
@login_required
def delete_js(request, id):
    js = JavaScript.objects.get(id=id)
    if request.method == 'POST':
        js.delete()
        return redirect('/')
    context = {
        'js': js
    }
    return render(request, 'crud/delete_js.html', context)

# delete
@login_required
def delete_py(request, id):
    py = Python.objects.get(id=id)
    if request.method == 'POST':
        py.delete()
        return redirect('/')
    context = {
        'py': py
    }
    return render(request, 'crud/delete_py.html', context)