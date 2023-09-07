from django.urls import path
from .views import *

app_name = 'detail'

urlpatterns = [
    path('html_css/<int:pk>/', html_css_detail, name='html_css_detail'),
    path('js/<int:pk>/', js, name='js_detail'),
    path('py/<int:pk>/', py, name='py_detail'),
]
