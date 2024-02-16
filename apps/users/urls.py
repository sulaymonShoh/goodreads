from django.urls import path
from apps.users.views import LoginView, RegisterView, LogoutView

# app_name = "auth"
urlpatterns = [
    path('register', RegisterView.as_view(), name="register"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
]
