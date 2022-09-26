from django.urls import path, include
from . import views

app_name = "access"

urlpatterns = [
    path(
        "",
        views.UserLoginView.as_view(),
    ),
    path("sign-in/", views.UserLoginView.as_view(), name="login"),
    path("sign-up/", views.UserRegisterView.as_view(), name="register"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
]
