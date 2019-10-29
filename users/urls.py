from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('register/', views.register, name='users-register'),
    path('profile/', views.profile, name='users-profile'),
]