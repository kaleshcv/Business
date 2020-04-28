# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def destinations(req):

    template=loader.get_template("destination.html")
    data={}
    res=template.render(data,req)
    return HttpResponse(res)