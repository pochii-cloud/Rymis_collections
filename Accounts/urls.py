from django.urls import path
from django.contrib.auth import views as auth_views
from Accounts.views import RegisterUser, LoginPage, LogoutPage,ProfilePage

urlpatterns = [
    path('RegisterUser/', RegisterUser.as_view(), name='RegisterUser'),
    path('LoginPage/', LoginPage.as_view(), name='LoginPage'),
    path('LogoutPage/', LogoutPage.as_view(), name='LogoutPage'),
    path('ProfilePage/', ProfilePage.as_view(), name='ProfilePage'),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="password_reset/password_reset_email.html"),
         name='reset_password'),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="password_reset/password_reset_sent.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="password_reset/password_reset_form.html"
    ), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="password_reset/password_reset_complete.html"
    ), name='password_reset_complete'),
]
