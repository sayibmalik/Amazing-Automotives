from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('team/', views.team, name='team'),
    path('gallery/', views.gallery, name='gallery'),
    path('testmonial/', views.testmonial, name='testmonial'),
]
