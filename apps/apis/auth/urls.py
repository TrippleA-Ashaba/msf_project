from django.urls import path

from .views import (
    LoginAPIView,
    LogoutAPIView,
    PasswordChangeAPIView,
    ResetPasswordAPIView,
    SignUpAPIView,
)

urlpatterns = [
    path("signup/", SignUpAPIView.as_view(), name="signup_api"),
    path("login/", LoginAPIView.as_view(), name="login_api"),
    path("logout/", LogoutAPIView.as_view(), name="logout_api"),
    path(
        "password_change/", PasswordChangeAPIView.as_view(), name="password_change_api"
    ),
    path("reset_password/", ResetPasswordAPIView.as_view(), name="reset_password_api"),
]
