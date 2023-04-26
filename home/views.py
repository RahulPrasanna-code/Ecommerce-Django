from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from products.models import Buyer,Product

# Create your views here.
def home_page(request):
    context = {}
    return render(request,'home/home_page.html',context)