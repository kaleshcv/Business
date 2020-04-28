from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Product


# Create your views here.

def home(req):
    template = loader.get_template('index.html')
    items = Product.objects.all()
    data = {'product': items}
    res = template.render(data,req)
    return HttpResponse(res)

def blog(req):
    template = loader.get_template('blog.html')
    #items = Product.objects.all()
    data = {}
    res = template.render(data,req)
    return HttpResponse(res)