from django.shortcuts import render
from .models import Product

from django.shortcuts import render
from .models import Product

from django.shortcuts import get_object_or_404, redirect
from .models import Cart

from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, redirect

from django.shortcuts import render, get_object_or_404

#Create your views here
def home(request):

    query = request.GET.get('search')

    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    return render(request, 'cover/home.html', {
        'products': products,
        'query': query
    })
def about(request):
    return render(request, "cover/about.html")


def contact(request):
    return render(request, "cover/contact.html")


def suggestions(request):
    return render(request, "cover/suggestions.html") 

def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    cart_item, created = Cart.objects.get_or_create(product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER', 'home'))


def cart(request):

    items = Cart.objects.all()

    total = 0

    for item in items:
        total += item.total_price()

    return render(request, "cover/cart.html", {
        "items": items,
        "total": total
    })  
def increase_quantity(request, cart_id):

    item = get_object_or_404(Cart, id=cart_id)

    item.quantity += 1
    item.save()

    return redirect("cart")


def decrease_quantity(request, cart_id):

    item = get_object_or_404(Cart, id=cart_id)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect("cart")


def remove_from_cart(request, cart_id):

    item = get_object_or_404(Cart, id=cart_id)

    item.delete()

    return redirect("cart") 

def checkout(request):

    return render(request, "cover/checkout.html")



def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(
        request,
        "cover/product_detail.html",
        {
            "product": product
        }
    )


