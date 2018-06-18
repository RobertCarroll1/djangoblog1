from django.urls import path
from accounts.views import login, register, logout, profile

urlpatterns = [
    path('login', login, name="login"),
    path('register', register, name="register"),
    path('logout', logout, name="logout"),
    path('profile', profile, name="profile"),
]