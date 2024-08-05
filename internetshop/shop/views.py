from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    products = []
    return render(request, "index.html", context={
        'product':products
    })

def view_product(request):
    return render(request, template_name='product.html')