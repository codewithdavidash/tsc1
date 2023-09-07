from django.urls import path
from .views import *

urlpatterns = [
    path('add/', add, name='add'),
    path('create_html_css/', create_html_css, name='create_html_css'),
    path('create_js/', create_js, name='create_js'),
    path('create_py/', create_py, name='create_py'),
    path('update_html_css/<int:id>/', update_html_css, name='update_html_css'),
    path('update_js/<int:id>/', update_js, name='update_js'),
    path('update_py/<int:id>/', update_py, name='update_py'),
    path('delete_html_css/<int:id>/', delete_html_css, name='delete_html_css'),
    path('delete_js/<int:id>/', delete_js, name='delete_js'),
    path('delete_py/<int:id>/', delete_py, name='delete_py'),
]
