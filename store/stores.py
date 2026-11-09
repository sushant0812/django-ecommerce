# store/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Product, OrderItem
from .cart import Cart
from .forms import OrderCreateForm

def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'store/product_list.html', {'products': products})

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=1)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'store/cart_detail.html', {'cart': cart})

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear() # Empty the cart after successful order creation
            return render(request, 'store/order_created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'store/order_create.html', {'cart': cart, 'form': form})
