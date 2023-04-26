from ast import Not
from itertools import product
from multiprocessing import context
from tkinter.messagebox import NO
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render,redirect
from products.models import Seller,Product
from users.forms import LoginUserForm
from sellers.forms import CreateProductForm, UpdateProductForm
from django.contrib.auth import authenticate,login

def seller_dashboard(request):
    user = request.user
    try:
        seller = Seller.objects.get(user=user)
    except:
        seller = None
    context = {}
    if seller is None:
        return render(request,'sellers/seller_intro_page.html',context)
    
    products = Product.objects.filter(seller=seller)
    context['user']=user
    context['seller']=seller
    context['products']=products


    return render(request,'sellers/seller_dashboard.html',context)

def seller_intro_page(request):
    context={}
    return render(request,'sellers/seller_intro_page.html',context)

def seller_login(request):
    if request.method=='POST':
        form = LoginUserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request,username=username,password=password)
            
            if user is not None:
                seller = Seller.objects.filter(user=user)
                if seller.exists():
                    login(request,user=user)
                    return redirect('seller_dashboard')
                else:
                    form.add_error('username','User is not a Seller')
            else:
                form.add_error('username','Invalid credentials')
    else:
        form = LoginUserForm()

    try:
        seller = Seller.objects.get(user=request.user)
    except Seller.DoesNotExist:
        seller=None
    if seller is not None:
        return redirect('seller_dashboard')
    context = {
        'form':form
    }
    return render(request,'sellers/seller_login.html',context)

def seller_detail_view(request,product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return HttpResponse('Not Found')

    context = {
        'product':product
    }
    return render(request,'sellers/detail_view.html',context)

def delete_products(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id',-1)

        if product_id == -1:
            raise Http404("Not Found")
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise Http404("Product Not Found")


        product.delete()
        return redirect('seller_dashboard') 

def create_product(request):
    seller = Seller.objects.get(user=request.user)
    form = CreateProductForm()
    if request.method == "POST":
        form = CreateProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            product.seller.add(seller)
            return redirect('seller_dashboard')
        else:
            raise Http404(form.errors)

    context = {
        'form':form
    }
    return render(request,'sellers/create_product.html',context)

def update_product_view(request,product_id):
    product = Product.objects.get(pk=product_id)
    form = UpdateProductForm(instance=product)
    
    context = {
        'form':form,
        'product':product
    }
    return render(request,'sellers/update_product.html',context)

def update_product(request):
    if request.method == "POST":
        product_id = request.POST['product_id']
        product = Product.objects.get(pk=product_id)
        form = UpdateProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('seller_detail_view',product_id=product_id)
        else:
            raise Http404(form.errors)
    
    return redirect('update_product',product_id=product_id)