from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as viewss


urlpatterns = [
    path("Signup/", views.CreateUser.as_view(), name="Signup"),
    path("Login/", LoginView.as_view(template_name="login.html"), name="Login"),    
    path("Logout/", views.singout, name="logout"),
    path('password_reset/', viewss.PasswordResetView.as_view(template_name='recover/password_reset.html'), name='password_reset'),
    path('password_reset/done/', viewss.PasswordResetDoneView.as_view(template_name='recover/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', viewss.PasswordResetConfirmView.as_view(template_name='recover/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', viewss.PasswordResetCompleteView.as_view(template_name='recover/password_reset_complete.html'), name='password_reset_complete'),

    ]




