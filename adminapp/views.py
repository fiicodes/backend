from unicodedata import category, name
from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def adminindex(request):
    return render(request,"backend/index.html")


def addcategory(request):
    if request.method=="POST":
        cname=request.POST["category"]
        image=request.FILES["image1"]
        check=Category.objects.filter(categoryname=cname)
        if check:
            return render(request,"backend/category.html",{'msg':"category exist!!"})
        else:
            add=Category(categoryname=cname,image=image)
            add.save()
            return render(request,"backend/index.html",{'msg':"submitted"})
            

    else:
        return render(request,"backend/category.html")

def productpage(request):
    categorys=Category.objects.all()
    return render(request,'backend/productadd.html',{'categorys':categorys})

def addproducts(request):
    if request.method=="POST":
        name=request.POST["name"]
        price=request.POST["price"]
        quantity=request.POST["quantity"]
        image=request.FILES["image1"]

        cid=request.POST.get('category')
        category=Category.objects.get(id=cid)
        
        check=Products.objects.filter(name=name)
        if check:
            return render(request,"backend/productadd.html",{'msg':"product exist!!"})
        else:
            add=Products(name=name,quantity=quantity,price=price,image=image,categoryeid=category)
            add.save()
            return render(request,"backend/index.html",{'msg':"submitted"})
            

    else:
        return render(request,"backend/productadd.html")


def billdetail(request):
    bill=Bill.objects.all()
    return render(request,'backend/billdetail.html',{'bill':bill})



def cartdetail(request):
    cart=Cart.objects.all()
    return render(request,'backend/cartdetail.html',{'cart':cart})


def producttable(request):
    product=Products.objects.all()
    return render(request,'backend/producttable.html',{'product':product})


def categorytable(request):
    category=Category.objects.all()
    return render(request,'backend/categorytable.html',{'category':category})