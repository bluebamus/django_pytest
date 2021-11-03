from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Product

# Create your views here.

@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk = pk)
    return render(request, 'product_dtail.html',{'product':product})