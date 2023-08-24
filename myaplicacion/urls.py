from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import login_view
from .views import home





urlpatterns = [
    path("", views.index, name="index"),
    path('landing/', views.landing, name='landing'),
    path('user-list/', views.user_list, name='user_list'),
    path('registro-usuario', views.registro_usuario, name='registro_usuario'),
    path('registro-exitoso/', views.registro_exitoso, name='registro_exitoso'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', login_view, name='login'),
    path('home/', home, name='home'),
    path('registro_usuario/', views.registro_usuario, name='registro_usuario'),
    path('home/', views.home, name='home'),
]














