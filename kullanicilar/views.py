from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout


def home(request):
    # registration page
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Notlar:index')
    else:
        form = UserCreationForm()
    return render(request, 'kullanici.html', {'form': form})


def home2(request):
  
    return render(request, 'giris.html')


def logout_view(request):
    
    logout(request)
    return redirect('giris')
    