from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from core.models import (
    HTML_CSS,
    JavaScript,
    Python
)


@login_required
def html_css_detail(request, pk):
    html_css = get_object_or_404(HTML_CSS, pk=pk)
#    js = get_object_or_404(JavaScript, pk=pk)
#    py = get_object_or_404(Python, pk=pk)
    context = {
        'html_css': html_css,
        #        'js': js,
        #        'py': py,
    }
    return render(request, 'detail/html_css_detail.html', context)


@login_required
def js(request, pk):
    js = get_object_or_404(JavaScript, pk=pk)
    context = {
        'js': js,
    }
    return render(request, 'detail/js_detail.html', context)


@login_required
def py(request, pk):
    py = get_object_or_404(Python, pk=pk)
    context = {
        'py': py,
    }
    return render(request, 'detail/py_detail.html', context)
