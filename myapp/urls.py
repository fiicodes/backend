from django.shortcuts import render

from django.urls import path,include
from django import urls
from myapp import views

urlpatterns = [
  
    path("",views.userindex,name="userindex"),
    path("categorylist/",views.categorylist,name="categorylist"),
    path("productlist/",views.productlist,name="productlist"),
    path("userregistration/",views.userregistration,name="userregistration"),
    path("login/",views.login,name="login"), 
    path("logout/",views.logout,name="logout"), 
    path("cart/",views.cart,name="cart"), 
    path("product_addcart/",views.product_addcart,name="product_addcart"),  
    path("delete_cartitem/",views.delete_cartitem,name="delete_cartitem"), 
    path("payment/",views.payment,name="payment"),
    path("makepayments/",views.makepayments,name="makepayments"),
    
    path("clearcart/",views.clearcart,name="clearcart"),
   

]

