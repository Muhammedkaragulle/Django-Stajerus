from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('kullanici/', views.home, name='kullanici'),
    path('giris/', auth_views.LoginView.as_view(template_name='giris.html'), name='giris'),
    path('logout/', views.logout_view, name='logout'),

   
    path(
        'forgot-password/',
        auth_views.PasswordResetView.as_view(
            template_name='forgot_password.html',
            html_email_template_name='forgot_password_email.html',
            subject_template_name='forgot_password_subject.txt',
            success_url=reverse_lazy('password_reset_done'),
        ),
        name='password_reset',
    ),

    path(
        'forgot-password/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='forgot_password_done.html'),
        name='password_reset_done',
    ),

    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='reset_password.html',
            success_url=reverse_lazy('password_reset_complete'),
        ),
        name='password_reset_confirm',
    ),

    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(template_name='reset_password_complete.html'),
        name='password_reset_complete',
    ),
]
