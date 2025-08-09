from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('subscribe/', views.subscribe, name="subscribe")
]
