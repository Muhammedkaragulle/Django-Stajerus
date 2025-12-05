from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='anasayfa'),
    path('Hakkimizda/',views.hakkimiz,name='Hakkimizda'),
    path('Bize-Ulasin/',views.ulas,name='Ulas'),
    path('Notlar/', include('Notlar.urls')),
    path('kullanicilar/', include('kullanicilar.urls')),
    path('admin/', admin.site.urls),
]

