from django.urls import path
from . import views

app_name = 'Notlar'

urlpatterns = [
    path('', views.home, name='index'),
]
