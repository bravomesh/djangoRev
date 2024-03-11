from django.shortcuts import render
from .forms import ProductForm
from .models import Product
# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'object':obj 
        # 'title':obj.title,
        # 'd':obj.description,
        # 'price':obj.price
    }
    return render(request, 'products/product_detail.html',context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=ProductForm()
        
    context={
        'form': form
    }
    
    return render(request, 'products/product_create.html', context)
    