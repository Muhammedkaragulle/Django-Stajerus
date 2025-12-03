from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # registration (keeps same name used in templates)
    path('kullanici/', views.home, name='kullanici'),
    # login using Django's built-in view; template is kullanicilar/giris.html
    path('giris/', auth_views.LoginView.as_view(template_name='giris.html'), name='giris'),
    # use our custom logout view so logout can run project-specific logic
    path('logout/', views.logout_view, name='logout'),
]
