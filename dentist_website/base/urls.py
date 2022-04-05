from django.urls import URLPattern, path 
from . import views

urlpatterns= [
    path ('', views.home),
    path ('home.html', views.home, name='home'),
    path ('about.html', views.about, name= 'about'),
    path ('contact.html', views.contact, name= 'contact'),
    path ('appointment.html', views.appointment, name= 'appointment'),
    path ('services.html', views.services, name = 'services'),
  
]