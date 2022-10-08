from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
  products = Product.objects.all()
  return render(request, 'index.html', {'products':products})
  # return HttpResponse('<h1>Welcome to Shopping Website home page<h1>')

def about(request):
  return HttpResponse('<h1>About Page</h1>')

def contact(request):
  return HttpResponse('<h1>Contact Page<h1>')

def cart(request):
  return HttpResponse('<h1>Cart</h1>')
