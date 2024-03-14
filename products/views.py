from django.shortcuts import render
from django.http import Http404
from .forms import ProductForm, RawProductForm
from .models import Product
# Create your views here.
def product_detail_view(request, my_id):
    try:
        obj = Product.objects.get(id=my_id)
    except Product.DoesNotExist:
        raise Http404('Product does not exist')
    context = {
        'object':obj 
        # 'title':obj.title,
        # 'd':obj.description,
        # 'price':obj.price
    }
    return render(request, 'products/product_detail.html',context)

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form=ProductForm()
        
#     context={
#         'form': form
#     }
    
#     return render(request, 'products/product_create.html', context)

def product_create_view(request):
    initial_data={
        'title':'this awesome title',
        'description':'this awesome description is okayg'
    }
    form = ProductForm(request.POST or None, initial = initial_data)
    
    context={ 
        'form': form
    }
    return render(request, 'products/product_create.html', context)