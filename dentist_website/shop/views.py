from django.shortcuts import render

# Create your views here.
def shop(request):
    return render(request, 'shop/main.html')
def checkout(request):
    return render(request, 'shop/checkout.html')
def cart(request):
    return render(request, 'shop/cart.html')
def store(request):
    return render(request, 'shop/main.html')