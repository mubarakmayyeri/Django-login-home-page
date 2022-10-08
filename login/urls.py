from operator import index
from django.urls import path
from . import views
from products import views as pview
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', LoginView.as_view(), name='userLogin'),
    path('about', pview.about, name='about'),
    path('contact', pview.contact, name='contact'),
    path('userRegister', views.userRegister, name='userRegister'),
]
