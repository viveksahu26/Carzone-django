from django.urls import path
from cars import views

urlpatterns = [
    path ('cars/',views.cars,name='cars'),
    path('<int:id>/', views.cardetails, name='cardetails'),
    path('search/', views.search, name='search'),
]