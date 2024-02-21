from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.handleLogin, name="Login"),
    path('register/', views.register, name="Register"),
    path('register-success/', views.register_success, name="registerSuccess"),
    path('logout/', views.handleLogout, name="Logout"),
    path('reserve/', views.reserve, name="Reserve"),
    path('about/', views.about, name="AboutUs"),
    path('menu/', views.menu, name="Menu"),
    path('contact/', views.contact, name="ContactUs"),
    path('profile/', views.user_profile, name='userProfile'),

]