from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path('landing/', views.landing, name='landing'),
    path('user-list/', views.user_list, name='user_list'),
    
]

