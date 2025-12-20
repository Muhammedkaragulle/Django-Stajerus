from django.urls import path
from . import views

app_name = 'Notlar'

urlpatterns = [
    path('', views.home, name='index'),
    path('public/', views.public_courses, name='public_courses'),
    path('public/<str:course_name>/', views.public_course_detail, name='public_course_detail'),
    path('note/<int:note_id>/like/', views.toggle_like, name='note_like'),
    path('note/<int:note_id>/dislike/', views.toggle_dislike, name='note_dislike'),
    path('note/<int:note_id>/comment/', views.add_comment, name='note_comment'),
]
