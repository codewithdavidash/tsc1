from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from .views import *
from .forms import LoginForm, ChangePassword

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',
         authentication_form=LoginForm), name='login'),
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='core/changepassword.html',
         form_class=ChangePassword, success_url=reverse_lazy('changepassworddone')), name='changepassword'),
    path('changepassworddone/', auth_views.PasswordChangeDoneView.as_view(template_name='core/changepassworddone.html'), name='changepassworddone'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('search/', search, name='search'),
    path('menu/', menu, name='menu'),
    path('delete_accounts/', delete_accounts, name='delete_accounts'),
    path('user_accounts/<int:id>/', user_accounts, name='user_accounts'),
    path('terms_and_conditions/', terms_and_conditions, name='terms_and_conditions')
]
