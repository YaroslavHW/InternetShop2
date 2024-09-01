import telebot
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Product
from .models import Review

API_TOKEN = '<7077276665:AAHBj6gWKhA7_MwA6pkwqyQxTg2kWxnsE64>'
CHAT_ID = 6670641282
bot = telebot.TeleBot(API_TOKEN)
# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, "index.html", context={
        'products': products
    })

def view_product(request, id):
    product = Product.objects.filter(id=id).first()

    if request.method == "POST":
        author = request.POST.get('author')
        rating = request.POST.get('rating')
        text = request.POST.get('text')
        review = Review(author=author, rating=int(rating), text=text,product=product)
        review.save()

    reviews = product.review_set.all()

    return render(request, template_name='product.html', context={
        'product': product,
        'reviews': reviews
    })
def payment(request):
    product = Product.objects.filter(id=id).first()

    if request.method == "POST":
        name = request.POST.get('fullname')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        bot.send_message(CHAT_ID, f'''Заказ: {product.name}\n\n ФИО заказчика: {name}\n Адрес: {address}\n Телефон: {phone}\n''')
        return redirect()

    return render(request, template_name='payment.html', context={
    'product': product,

    })

def payment_success(request):
    return render(request, template_name='success.html')