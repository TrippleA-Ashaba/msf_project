from django.urls import path
from .views import SignUpAPIView, LoginAPIView, LogoutAPIView

urlpatterns = [
    path("signup/", SignUpAPIView.as_view(), name="signup_api"),
    path("login/", LoginAPIView.as_view(), name="login_api"),
    path("logout/", LogoutAPIView.as_view(), name="logout_api"),
]
