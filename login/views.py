from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def userLogin(request):
  return render(request, 'login.html',)

def userRegister(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('userLogin')
  else:
    form = UserCreationForm()
  return render(request, 'register.html',{'form':form})
