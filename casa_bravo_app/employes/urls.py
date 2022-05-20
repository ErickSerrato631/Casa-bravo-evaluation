from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'alta_data'

urlpatterns = [
   #------------------------------------- CRUD employes ------------------------------------------------------
    path('employe/list', views.EmployeListView.as_view(), name='employes_list'),
    path('employe/create', views.EmployeCreateView.as_view(), name='employes_create'),    
    path('employe/detail/<pk>/', views.EmployeDetailView.as_view(), name='employes_detail'),   
    path('employe/delete/<pk>/', views.EmployeDeleteView.as_view(), name='employes_delete'),  
    path('employe/update/<pk>/', views.EmployeUpdateView.as_view(), name='employes_update'),    
]