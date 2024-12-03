from django.views.generic import CreateView, DetailView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Order, Payment
from cart.models import CartItem
from django.contrib.auth.decorators import login_required 


class OrderCreateView(CreateView):
    model = Order
    fields = ('address', 'phone_number',)
    template_name = 'create_order.html'
    success_url = reverse_lazy('orders-page')
    
    def form_valid(self, form):  
        cart_items = CartItem.objects.filter(order_id=None)
        total = 0
        for cart_item in cart_items:  
            total += cart_item.product.price * cart_item.amount
        form.instance.total = total
        order = super().form_valid(form)
        cart_items.update(order_id=self.object.id)
        return order
    
class PaymentCreateView(CreateView):
    model = Payment
    fields = ('card_number', 'Person_name', 'Expiry', 'cvv')
    template_name = 'create_payment.html'
    success_url = reverse_lazy('orders-page')
    def form_valid(self, form):
        form.instance.order_id = self.kwargs.get('order_id')
        return super().form_valid(form)

@login_required
def order_list_view(request):
    if request.method == 'GET':
        qs = Order.objects.order_by('-created_at')
        return render(request, 'orders.html', {'orders': qs})
    elif request.method == 'POST':
        order_id = request.POST.get('delete_order')
        if order_id:
            try:
                order = Order.objects.get(pk=order_id)
                CartItem.objects.filter(order=order).delete()
                order.delete()
            except Order.DoesNotExist:
                pass  
    return redirect('orders-page')

class OrderDetailView(DetailView):
    model = Order
    slug_field = 'id'
    slug_url_kwarg = 'order_id'
    template_name = 'orders_details.html' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = self.get_object()
        cart_items = CartItem.objects.filter(order=order)
        for cart_item in cart_items:
            cart_item.total_price = cart_item.product.price * cart_item.amount
        context['object_list'] = cart_items
        return context
# Create your views here.
