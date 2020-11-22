from django.urls import path
from servo import views

urlpatterns = [
    path("", views.home, name="home"),
]
