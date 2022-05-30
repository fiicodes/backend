
from unicodedata import category
from django.shortcuts import render
from django.http import *
from adminapp.models import *
import random
import string
import hashlib
import datetime


# Create your views here.
def userindex(request):
    return render(request, "userindex.html")


def categorylist(request):
    category = Category.objects.all()
    return render(request, "categorylist.html", {"category": category})


def productlist(request):
    ii = request.GET['id']
    p = Products.objects.filter(categoryeid=ii)
    return render(request, "productlist.html", {"p": p})


def userregistration(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmpassword = request.POST["confirmpassword"]
        hashpass = hashlib.md5(password.encode('utf8')).hexdigest()

        check = User.objects.filter(email=email)
        if check:
            return render(request, "register.html", {'msg': "User exist!!"})
        else:
            if password == confirmpassword:
                x = ''.join(random.choices(name+string.digits, k=8))
                y = ''.join(random.choices(
                    string.ascii_letters+string.digits, k=7))

                add = User(name=name, email=email,
                           password=password, hashpassword=hashpass)

                add.save()
                return HttpResponseRedirect('/')
    else:

        return render(request, "register.html")


def login(request):
    if request.method == "POST":

        cname = request.POST["name"]
        cpass = request.POST["password"]
        print(cpass, "))))))")
        hashpass = hashlib.md5(cpass.encode('utf8')).hexdigest()

        log = User.objects.filter(name=cname, hashpassword=hashpass)
        if log:
            for x in log:
                request.session["myid"] = x.id
                request.session["myname"] = x.name
                ii = request.session["myid"]
            #    request.session["img"]=x.image.url
            #    uid = teacher_tb.objects.filter(id=ii)
            #    if uid:
                return render(request, "userindex.html")
            #    else:

            #       return render(request,'loginteach.html')
        else:
            return render(request, "login.html", {"msg": "invalid credentials"})
    else:
        return render(request, "login.html")


def logout(request):
    if request.session.has_key('myid'):
        del request.session["myid"]
        del request.session["myname"]
        logout(request)
        return HttpResponseRedirect('/')


def product_addcart(request):
    if request.session.has_key('myid'):
        if request.method == 'POST':
            pids = request.GET['id']
            petdet = Products.objects.all().filter(id=pids)
            for x in petdet:
                unitprice = x.price
            qty = request.POST['qty']
            shipping = int(int(unitprice)*10/100)
            total = int(unitprice)*int(qty)+shipping
            date = datetime.datetime.now()
            ii = request.session["myid"]
            print(ii)
            uid = User.objects.get(id=ii)
            x = datetime.datetime.now()
            pid = Products.objects.get(id=pids)
            ii = User.objects.get(id=ii)
            check = Cart.objects.all().filter(user_id=ii, product_id=pids,
                                              price=unitprice, total=total, date=date)
            if check:
                mypet = Cart.objects.all().filter(user_id=ii, status='pending')
                return render(request, 'cart.html', {'uv': mypet, 'msgkey': 'Already Add to cart'})
            else:
                tocart = Cart(user_id=ii, product_id=pid, price=unitprice,
                              total=total, date=date, quantity=qty)
                tocart.save()
                thispet = Products.objects.all().filter(id=pids)
                for x in thispet:
                    oldqty = x.quantity
                newqty = int(oldqty)-int(qty)
                Products.objects.all().filter(id=pids).update(quantity=newqty)
                mycart = Cart.objects.all().filter(user_id=ii, status='pending')
                grandtotal = 0
                for x in mycart:
                    grandtotal = int(x.total)+grandtotal

        grandtotal = grandtotal-500 if grandtotal > 10000 else grandtotal

        mypet = Cart.objects.all().filter(user_id=ii, status='pending')
        return render(request, 'cart.html', {'uv': mypet, 'gt': grandtotal, 'msgkey': 'Add to cart'})
    else:
        print("*************************************************************")
        return render(request, 'login.html')


def cart(request):
    if request.session.has_key('myid'):
        ii = request.session['myid']
        mycart = Cart.objects.all().filter(user_id=ii, status='pending')
        grandtotal = 0
        for x in mycart:
            grandtotal = int(x.total)+grandtotal
        mypet = Cart.objects.all().filter(user_id=ii, status='pending')
        return render(request, 'cart.html', {'uv': mypet, 'gt': grandtotal})
    else:
        return render(request, 'login.html')


def delete_cartitem(request):
    ii = request.session['myid']
    cid = request.GET['id']
    cartitem = Cart.objects.all().filter(id=cid)
    for x in cartitem:
        itemid = x.product_id.id
        quantity = x.quantity
    petsdata = Products.objects.all().filter(id=itemid)
    for x in petsdata:
        oldqty = x.quantity
    newqty = int(oldqty)+int(quantity)
    Products.objects.all().filter(id=itemid).update(quantity=newqty)
    Cart.objects.all().filter(id=cid).delete()
    mycart = Cart.objects.all().filter(user_id=ii, status='pending')
    grandtotal = 0
    for x in mycart:
        grandtotal = int(x.total)+grandtotal
    grandtotal = grandtotal-500 if grandtotal > 10000 else grandtotal

    mypet = Cart.objects.all().filter(user_id=ii, status='pending')
    return render(request, 'cart.html', {'uv': mypet, 'gt': grandtotal, 'msg': 'Successfully deleted'})


def payment(request):
    if request.session.has_key('myid'):
        gt = request.GET['gt']
        if request.method == 'GET':
            pid = request.GET.get('id')
            ii = request.session['myid']
            prdview = Products.objects.filter(id=pid)
            usrview = User.objects.filter(id=ii)
            print(pid, "***********************")
            print(gt, "####")
            return render(request, "payment.html", {"prd": prdview, "usr": usrview, "amount": gt})
    else:
        return render(request, 'login.html')


def makepayments(request):
    if request.method == "POST":
        uid = request.POST['userid']
        ii = User.objects.get(id=uid)
        amount = request.POST['amount']

        x = datetime.datetime.now()
        check = Bill.objects.filter(user_id=ii, amount=amount, date=x)
        if check:
            return render(request, 'cart.html')
        else:
            Cart.objects.filter(user_id=ii).update(status="paid")
            add = Bill(user_id=ii, amount=amount, date=x, status="paid")
            add.save()

            return HttpResponseRedirect('/')


def clearcart(request):
    ii = request.session['myid']

    Cart.objects.all().filter(user_id=ii, status="pending").delete()
    return HttpResponseRedirect('/')
