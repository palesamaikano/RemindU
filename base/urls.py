from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("signup/", views.authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('reminders/', views.reminders_view, name='reminders'),
    path('todo/', views.todo_view, name='todo'),
]