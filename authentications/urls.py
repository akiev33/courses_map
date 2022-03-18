from django.urls import path, include

from authentications.views import UserRegisterApiView, UserProfileAPIView,\
                             EducationCentreProfileAPIView, TeacherProfileAPIView, NonProfitOrganizationProfileAPIView,\
                             EmployerProfileAPIView, ActivationView, LoginApiView, LogoutApiView, ChangePasswordView,\
                             AdminUserProfileAPIView, AdminEducationCentreProfileAPIView, AdminTeacherProfileAPIView,\
                             AdminNonProfitOrganizationProfileAPIView, AdminEmployerProfileAPIView


from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', UserRegisterApiView.as_view()),

    path('user_profile/<int:id>/', UserProfileAPIView.as_view()),
    path('education_centre_profile/<int:id>/', EducationCentreProfileAPIView.as_view()),
    path('teacher_profile/<int:id>/', TeacherProfileAPIView.as_view()),
    path('non_profit_org_profile/<int:id>/', NonProfitOrganizationProfileAPIView.as_view()),
    path('employer_profile/<int:id>/', EmployerProfileAPIView.as_view()),

    path('admin/user_profile/<int:id>/', AdminUserProfileAPIView.as_view()),
    path('admin/education_centre_profile/<int:id>/', AdminEducationCentreProfileAPIView.as_view()),
    path('admin/teacher_profile/<int:id>/', AdminTeacherProfileAPIView.as_view()),
    path('admin/non_profit_org_profile/<int:id>/', AdminNonProfitOrganizationProfileAPIView.as_view()),
    path('admin/employer_profile/<int:id>/', AdminEmployerProfileAPIView.as_view()),

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
