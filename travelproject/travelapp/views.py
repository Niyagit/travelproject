from django.http import HttpResponse
from django.shortcuts import render
from . models import product,travel
# Create your views here.
def demo(request):
    obj=product.objects.all()
    obj1=travel.objects.all()
    
    return render(request,'index.html',{'result':obj,'results':obj1})

def about(request):
    return render(request,'about.html')

def contact(request):
    return HttpResponse("Hello am contact")

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     k=x,y
#     res=x+y
#     ress=x-y
#     resm=x*y
#     resd=x/y
#     return render(request,"result.html",{'num':k,'result1':res,'result2':ress,'result3':resm,'result4':resd})


