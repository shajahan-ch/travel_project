from django.http import HttpResponse
from django.shortcuts import render
from. models import Place
from.models import new
# Create your views here.

def demo(request):
    obj=new.objects.all()
    return render(request,"index.html",{'result':obj})

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,'usual.html',{'result':res})

