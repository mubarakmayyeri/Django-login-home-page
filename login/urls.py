from operator import index
from django.urls import path
from . import views
from products import views as pview
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('about', pview.about, name='about'),
    path('contact', pview.contact, name='contact'),
    path('register', views.register, name='register'),
]
