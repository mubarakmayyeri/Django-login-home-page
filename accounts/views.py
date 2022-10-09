from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
  return render(request, 'home.html')

def userRegister(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('userLogin')
  else:
    form = UserCreationForm()
    
  return render(request, 'registration/register.html',{'form':form})
