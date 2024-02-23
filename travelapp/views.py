from django.http import HttpResponse
from django.shortcuts import render
from . models import Place,Testimonial

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj2=Testimonial.objects.all()
    return render(request,"index.html",{'result':obj,'testimony':obj2})

def addition(request):
    x=int(request.GET['num1'])
    y =int (request.GET['num2'])
    res=x+y
    return render(request,"result.html",{"result":res})

def contact(request):
    return render(request,"contact.html")

