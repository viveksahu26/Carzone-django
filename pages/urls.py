from django.urls import path
from pages import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('contact/', views.contact, name='contact'),
    path('logout/', views.logout, name='logout'),
    path('services/', views.services, name='services'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
]