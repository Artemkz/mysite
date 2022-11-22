from django.urls import path
from .import views

urlpatterns = [
    path('', views.stock_home, name='stock_home'),
    path('company/', views.company, name='company')
]