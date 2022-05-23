from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'base/home.html',{})
def about(request):
    return render(request, 'base/about.html',{})
def contact (request):
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