from itertools import product
from math import prod
from tkinter.messagebox import NO
from django.http import Http404
from django.shortcuts import redirect, render
from products.models import Buyer,OrderProduct,Product

# Create your views here.
def cart_view(request):
    try:
        buyer = Buyer.objects.get(user=request.user)
    except Buyer.DoesNotExist:
        buyer = None

    if buyer is None:
        return redirect('home_page')

    cart_items = OrderProduct.objects.filter(buyer = buyer)
    context = {
        'cart_items':cart_items
    }
    return render(request,'cart/cart_view.html',context)

def add_to_cart(request):
    try:
        buyer = Buyer.objects.get(user=request.user)
    except Buyer.DoesNotExist:
        buyer = None

    if buyer is None:
        return redirect('home_page')

    if request.method == "POST":
        product_id = request.POST.get('product_id',None)
        if product_id is None:
            raise Http404('Product Not found')
        product = Product.objects.get(id=product_id)

        quantity = request.POST.get('quantity',1)

        try:
            order_product = OrderProduct.objects.get(product=product)
        except OrderProduct.DoesNotExist:
            order_product = None

        if order_product is not None:
            order_product.quantity=quantity
            order_product.save()
            return redirect('cart_view')
        else:
            new_order_product = OrderProduct.objects.create(buyer=buyer,product=product,quantity=quantity)
            new_order_product.save()
            return redirect('product_detail_view',product_id=product_id)

def delete_from_cart(request):
    if request.method=='POST':
        item_id = request.POST.get('item_id',-1)
        if item_id != -1:
            item = OrderProduct.objects.get(id=item_id)
            item.delete()
            return redirect('cart_view')
        else:
            raise Http404("Not a success")