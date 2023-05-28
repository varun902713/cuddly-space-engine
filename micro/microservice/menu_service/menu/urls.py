from django.contrib import admin
from django.urls import path
from menu import views
urlpatterns = [
    path('restaurants/', views.RestaurantListCreateView.as_view(), name='restaurant_getlist'),
    path('restaurants/<int:pk>/', views.RestaurantRetrieveUpdateDestroyView.as_view(), name='restaurant_crud'),
]