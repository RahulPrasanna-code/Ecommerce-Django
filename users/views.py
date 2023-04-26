from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import CreateUserForm,LoginUserForm
from django.contrib.auth.models import User
from products.models import Buyer,Seller
from django.contrib.auth import login,authenticate

def admin_create_buyer(request):
    if request.method=='POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            display_name = form.cleaned_data['display_name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']
            contact_no = form.cleaned_data['contact_no']
            user = User.objects.create_user(username=username,password=password,first_name=display_name)
            if user is not None:
                buyer = Buyer.objects.create(user = user,contact=contact_no)
                buyer.save()
                login(request=request,user=user)
                return redirect('home')
    else:
        form = CreateUserForm()

    context = {'form':form}

    return render(request,'users/create_user.html',context)

def home(request):
    try:
        buyer = Buyer.objects.get(user=request.user)
    except Buyer.DoesNotExist:
        buyer = None
    return render(request,'users/success_page.html',{})


def login_user(request):

    try:
        user = request.user
    except User.DoesNotExist:
        user = None
    
    if user is not None:
        try:
            buyer = Buyer.objects.get(user=user)
        except Buyer.DoesNotExist:
            buyer = None
        
        if buyer is not None:
            return redirect('products_page')


    if request.method=='POST':
        form = LoginUserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request,username=username,password=password)
            
            if user is not None:
                try:
                    buyer = Buyer.objects.filter(user=user)
                except Buyer.DoesNotExist:
                    buyer = None
                if buyer is not None:
                    login(request,user=user)
                    return redirect('products_page')
                else:
                    form.add_error('username','User is not a Buyer ')
            else:
                form.add_error('username','Invalid credentials')
    else:
        form = LoginUserForm()

    context = {
        'form':form
    }
    return render(request,'users/login_user.html',context)
