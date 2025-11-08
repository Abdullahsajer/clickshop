from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from store.models import Product
from .models import Order, OrderItem
from .forms import CheckoutForm  # Import the new form


# ✅ إضافة منتج إلى السلة (Order غير مدفوع)
@login_required
def add_to_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # ✅ جلب الطلب المفتوح أو إنشاء واحد جديد
    order, created = Order.objects.get_or_create(user=request.user, is_paid=False)

    # ✅ إضافة المنتج أو تحديث الكمية
    order_item, item_created = OrderItem.objects.get_or_create(
        order=order,
        product=product,
        defaults={'price': product.price, 'quantity': 1}
    )
    if not item_created:
        order_item.quantity += 1
        order_item.save()

    return redirect('orders:order_view')


# ✅ عرض السلة الحالية (Order بحالة is_paid=False)
@login_required
def order_view(request):
    order = Order.objects.filter(user=request.user, is_paid=False).first()
    return render(request, 'orders-templates/cart.html', {'order': order})


# ✅ صفحة إتمام الطلب (Checkout)
@login_required
def checkout_view(request):
    order = Order.objects.filter(user=request.user, is_paid=False).first()
    if not order or not order.items.exists():
        return redirect('orders:order_view')

    if request.method == 'POST':
        # ✅ استخدام النموذج للتحقق من صحة البيانات وحفظها
        form = CheckoutForm(request.POST, instance=order)
        if form.is_valid():
            form.save()  # Saves the order with updated user details
            order.is_paid = True  # Mark the order as paid
            order.save()
            return redirect('orders:order_success', order_id=order.id)
        else:
            # If form is not valid, re-render the checkout page with errors
            return render(request, 'orders-templates/checkout.html', {'order': order, 'form': form})
    else:
        # If GET request, pre-fill the form with existing order data
        form = CheckoutForm(instance=order)
        return render(request, 'orders-templates/checkout.html', {'order': order, 'form': form})


# ✅ صفحة نجاح الطلب بعد الإتمام
@login_required
def order_success_view(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user, is_paid=True)
    return render(request, 'orders-templates/order_success.html', {'order': order})


# ✅ عرض كل الطلبات السابقة للمستخدم
@login_required
def orders_list_view(request):
    orders = Order.objects.filter(user=request.user, is_paid=True).order_by('-created_at')
    return render(request, 'orders-templates/orders_list.html', {'orders': orders})
