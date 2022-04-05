from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.

def home(request):
    return render(request, 'base/home.html',{})
def about(request):
    return render(request, 'base/about.html',{})
def contact (request):
   if request.method == 'POST':
      patron_name = request.POST['patron-name'] 
      patron_email = request.POST['patron-email']
      patron_subject = request.POST['patron-subject']
      patron_message = request.POST['patron-message']
     
                    
                    
                  #send an emai
      #send_mail(
       # patron_name, #name
        #patron_subject, # subject
        #patron_message, #message
        #patron_email, #from email
        #['akinoyetayo@rocketmail.com'], #To Email
        #)
      #return render(request, 'contact.html',{'patron_name':patron_name})
  
   #else:
   return render(request, 'base/contact.html')
 
def appointment (request):
    return render(request, 'base/appointment.html', {})
def services (request):
    return render(request, 'base/services.html', {})
def shop(request):
    
    return render(request, 'shop/main.html', {})
def checkout(request):
    return render(request, 'shop/checkout.html', {})
def cart(request):
    return render(request, 'shop/cart.html', {})
def store(request):
    return render(request, 'shop/main.html', {})