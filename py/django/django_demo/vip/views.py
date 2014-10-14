from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, vip index.")
    

def detail(request, id):
    return HttpResponse("You're looking at VIP {0}.".format(id))
    
    
def result(request, id):
    return HttpResponse("You're looking at result of VIP {0}.".format(id))
