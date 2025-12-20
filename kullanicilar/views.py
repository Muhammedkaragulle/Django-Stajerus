from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Gmail adresinizi girin')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("email",)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip()
        if not email.lower().endswith('@gmail.com'):
            raise forms.ValidationError('Lütfen @gmail.com uzantılı bir e-posta adresi girin.')
        # ensure email uniqueness
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Bu e-posta adresi zaten kullanılıyor.')
        return email


def home(request):
    # registration page
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Notlar:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'kullanici.html', {'form': form})


def home2(request):
  
    return render(request, 'giris.html')


def logout_view(request):
    
    logout(request)
    return redirect('giris')
    