from django.db import models
from Admin.models import *
#Create your models here.
class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_gender=models.CharField(max_length=10)
    user_contact=models.CharField(max_length=15)
    user_email=models.CharField(max_length=30)
    user_password=models.CharField(max_length=30)
    user_address=models.CharField(max_length=30)
    user_photo=models.FileField(upload_to='Assets/UserDocs/')
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    # user_status=models.IntegerField(default=0)
class tbl_seller(models.Model):
    seller_name=models.CharField(max_length=50)
    seller_contact=models.CharField(max_length=15)
    seller_email=models.CharField(max_length=30)
    seller_password=models.CharField(max_length=30)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    seller_establishdate=models.DateField(max_length=12)
    seller_licenseno=models.CharField(max_length=15)
    seller_ownername=models.CharField(max_length=50)
    seller_licenseproof=models.FileField(upload_to='Assets/SellerDocs/')
    seller_ownerproof=models.FileField(upload_to='Assets/SellerDocs/')
    seller_status=models.IntegerField(default=0)

class tbl_driver(models.Model):
    driver_name=models.CharField(max_length=50)
    driver_email=models.CharField(max_length=30)
    driver_contact=models.CharField(max_length=15)
    driver_address=models.CharField(max_length=30)
    driver_photo=models.FileField(upload_to='Assets/UserDocs/')
    driver_license=models.FileField(upload_to='Assets/UserDocs/')
    driver_password=models.CharField(max_length=30)
    driver_status=models.IntegerField(default=0)
    driver_doj=models.DateField(auto_now_add=True)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    
    
    