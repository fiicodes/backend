from django.db import models

# Create your models here.
class Category(models.Model):
    categoryname=models.CharField(max_length=200,default="")
    image=models.FileField(upload_to="categoryimage",default="" )





class User(models.Model):
    name=models.CharField(max_length=200,default="")
    
    email=models.CharField(max_length=200,default="")
    password=models.TextField(default="")
    hashpassword=models.TextField(default="")



class Products(models.Model):
    categoryeid=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.FileField(upload_to="product",default="" )

    
    name=models.CharField(max_length=200,default="")
    
    price=models.CharField(max_length=200,default="")
   
    quantity=models.CharField(max_length=200,default="")


class Bill(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.CharField(max_length=200,default="")
    amount=models.CharField(max_length=200,default="")
    status=models.CharField(max_length=200,default="pending")


class Cart(models.Model):
    product_id=models.ForeignKey(Products, on_delete=models.CASCADE)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    quantity=models.CharField(max_length=200,default="")
    price=models.CharField(max_length=200,default="")
    total=models.CharField(max_length=200,default="")
    date=models.CharField(max_length=200,default="")

    status=models.CharField(max_length=200,default="pending")
