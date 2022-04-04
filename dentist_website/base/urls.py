from django.urls import URLPattern, path 
from . import views

urlpatterns= [
    path ('', views.home),
    path ('home.html', views.home),
    path ('about.html', views.about),
    path ('contact.html', views.contact, name= 'contact'),
    path ('appointment.html', views.appointment),
    path ('services.html', views.services),
  
]