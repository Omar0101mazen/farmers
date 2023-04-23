from django.shortcuts import redirect, render
from .cart import Cart
from .models import *
from django.contrib.auth.decorators import login_required





def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return redirect('products:products')

def cart_view(request):
    cart = Cart(request)
    
    return render(request, 'cart/cart-checkout.html',{'cart':cart})

def remove_from_cart(request,product_id):
    cart = Cart(request)
    cart.remove(str(product_id))
    
    return redirect('cart:cart_view')

def change_quantity(request,product_id):
    cart = Cart(request)
    action = request.GET.get('action','')
    if action:
        quantity = 1
        
        if action  == 'decrease':
            quantity = -1
        cart.add(product_id,quantity,True)
    return redirect('cart:cart_view')  



@login_required
def start_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        full_names = request.POST.get('full_name')
        credit_card_names = request.POST.get('credit_card_name')
        credit_card_numbers = request.POST.get('credit_card_number')
        expiration_dates = request.POST.get('expiration_date')
        ccv = request.POST.get('ccv')
        
        order = Order.objects.create(user=request.user,full_name=full_names,credit_card_name=credit_card_names,
                                     credit_card_number=credit_card_numbers,
                                     expiration_date=expiration_dates,ccv=ccv)
        
        for item in cart:
            
            product = item['product']
            
            quantity = item['quantity']
            Price = product.prices *quantity

        
            item = OrderItem.objects.create(order=order,product=product,quantity=quantity,Price=Price)
        cart.clear()        
        
        return redirect('accounts:profile_user')
    
    return redirect('cart:cart_view')

