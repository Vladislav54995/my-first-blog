from django.shortcuts import redirect,render
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from .models import Cart, CartItem
from product.models import Product
from django.http import HttpResponse
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django.db.models import F, Sum, ExpressionWrapper, DecimalField

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    
    quantity = int(request.POST.get('quantity', 1))  # Получаем количество товара из формы
    
    # Добавляем товар в корзину или обновляем его количество
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product, order_id=None)
    if item_created:
        cart_item.amount = quantity
    else:
        cart_item.amount += quantity
    cart_item.save()
    
    messages.success(request, 'Товар добавлен в корзину!')
    return redirect('product-details-page', category_id=product.category.id, product_id=product.id)


@login_required
def cart_list_view(request):
    if request.method == 'POST':
        if 'create_order' in request.POST:
            return redirect('create-order-page')
        elif 'delete_item' in request.POST:
            delete_item_id = request.POST.get('delete_item')
            if delete_item_id:
                try:
                    cart_item = CartItem.objects.get(pk=delete_item_id, cart=request.user.cart)
                    cart_item.delete()
                except CartItem.DoesNotExist:
                    pass
            return redirect('cart-page')
        else:
            for item_id, quantity in request.POST.items():
                if item_id.startswith('quantity_'):
                    cart_item_id = int(item_id.split('_')[1])
                    quantity = int(quantity)
                    try:
                        cart_item = CartItem.objects.get(pk=cart_item_id, cart=request.user.cart)
                        cart_item.amount = quantity
                        cart_item.save()
                    except CartItem.DoesNotExist:
                        pass
            return redirect('cart-page')

    # Аннотация для общей стоимости по каждому элементу
    qs = CartItem.objects.filter(cart=request.user.cart, order_id=None)
    qs = qs.annotate(item_total=ExpressionWrapper(
        F('product__price') * F('amount'),
        output_field=DecimalField()
    ))

    # Подсчёт общей стоимости корзины
    total_price = qs.aggregate(total_price=Sum('item_total'))['total_price'] or 0

    return render(request, 'cart.html', {'object_list': qs, 'total_price': total_price})
