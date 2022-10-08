from operator import index
import django
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('cart', views.cart, name='cart'),
    path('loggedOut', LogoutView.as_view(next_page='login'), name='loggedOut')
]
