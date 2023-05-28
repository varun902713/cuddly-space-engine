from django.contrib import admin
from django.urls import path
from user import views
urlpatterns = [
    path("user/get",views.UserListView.as_view(),name='index'),
    path('user/<int:id>',views.UserDetailView.as_view(),name='user_creation'),
    path('user/login',views.login.as_view(),name='login'),
    path('user/validation',views.validation,name='validation')

]
