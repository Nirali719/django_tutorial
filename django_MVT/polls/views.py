from django.http import HttpResponse
from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request,"calc.html")

def add(request):
    val1=request.POST['num1']
    val2=request.POST['num2']
    res=int(val1)+int(val2)
    return render(request,'result.html',{'result':res})