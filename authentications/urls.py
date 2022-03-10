from django.urls import path, include
from authentications.views import RegisterApiView, ActivationView, LoginApiView, LogoutApiView, ChangePasswordView


from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('login/', LoginApiView.as_view(), name='login'),
    path('activate/<uuid:activation_code>/', ActivationView.as_view(), name='activate_account'),
    path('logout/', LogoutApiView.as_view()),
    path('change/', ChangePasswordView.as_view()),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='reset_password_sent'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done')
]