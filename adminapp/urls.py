from django.urls import path,include
from django import urls
from adminapp import views

urlpatterns = [
  
    path("",views.adminindex),
    path("addcategory/",views.addcategory,name="addcategory"),
    path("addproducts/",views.addproducts,name="addproducts"),
    path("productpage/",views.productpage,name="productpage"),
    path("cartdetail/",views.cartdetail,name="cartdetail"),
    path("billdetail/",views.billdetail,name="billdetail"),
    path("producttable/",views.producttable,name="producttable"),
    path("categorytable/",views.categorytable,name="categorytable"),

]
  
