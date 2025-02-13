# members/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('register/', views.register, name='register'),  # User registration
    path('login/', views.user_login, name='login'),  # User login
    path('logout/', views.user_logout, name='logout'),  # User logout
    path('dashboard/', views.dashboard, name='dashboard'),  # User dashboard
    path('add-bill/', views.add_bill, name='add_bill'),

    path('mark-paid/<int:bill_id>/', views.mark_paid, name='mark_paid'), 
    

]