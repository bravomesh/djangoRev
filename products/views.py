from django.shortcuts import render
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
    return render(request, 'product/detail.html',context)
    