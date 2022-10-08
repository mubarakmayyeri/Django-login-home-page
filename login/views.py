from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def login(request):
  return render(request, 'login.html',)

def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
  else:
    form = UserCreationForm()
  return render(request, 'register.html',{'form':form})
