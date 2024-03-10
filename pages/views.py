from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request,*args, **kwargs):
    context ={
        'banana':23,
        'lemon':[21,32,4,43,54,5,65]
    }
    return render(request,'home.html', context)

def about_view(request,*args, **kwargs):
    return render(request, 'about.html',{})