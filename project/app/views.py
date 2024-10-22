from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun1(req,a):
    print("hello")
    a=[10,11,12,13]
    type(a)
    return HttpResponse(a)
def fun2(req):
    return HttpResponse("habibi")