from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    products = [1]
    return render(request, "index.html", context={
        'products': products
    })

def view_product(request):
    return render(request, template_name='product.html')