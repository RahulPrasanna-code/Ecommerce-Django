from itertools import count
from django.http import Http404, HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from products.models import Product,Buyer,OrderProduct

# Create your views here.
def home(request):
    user = request.user
    try:
        buyer = Buyer.objects.get(user = user)
    except Buyer.DoesNotExist:
        buyer = None

    if buyer is None:
        return redirect('home_page')

    cart_items = OrderProduct.objects.filter(buyer=buyer)
    products = Product.objects.all()
    context = {
        'cart_items':cart_items,
        'user':user,
        'buyer':buyer,
        'products':products
    }
    return render(request,'products/home_page.html',context)

def product_detail_view(request,product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404('Product Not found')

    buyer = Buyer.objects.get(user=request.user)
    cart_items = OrderProduct.objects.filter(buyer=buyer)

    in_cart=False
    cart_item = None
    for item in cart_items:
        if product == item.product:
            in_cart = True
            cart_item=item
            break
    context = {
        'in_cart':in_cart,
        'cart_item':cart_item,
        'cart_items':cart_items,
        'product':product,
    }
    return render(request,'products/detail_view.html',context)


