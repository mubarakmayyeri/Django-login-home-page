from operator import index
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('userLogin', LoginView.as_view(), name='userLogin'),
    path('userRegister', views.userRegister, name='userRegister'),
    path('userLogout',LogoutView.as_view(next_page='userLogin'), name='userLogout')
]
