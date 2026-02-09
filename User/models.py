from django.db import models
from Admin.models import *
from Driver.models import *
from Guest.models import *
# Create your models here.
class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=50)
    complaint_content=models.CharField(max_length=50)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=50,null=True)
    complaint_status=models.IntegerField(default=0)
    user=models.ForeignKey(tbl_user, on_delete=models.CASCADE)

class tbl_booking(models.Model):
    booking_date=models.DateField(auto_now_add=True)
    booking_status=models.IntegerField(default=0)
    bookinguser_status=models.IntegerField(default=0)
    booking_amount=models.IntegerField(null=True)
    booking_advance=models.IntegerField(null=True)
    booking_days=models.IntegerField(null=True)
    booking_distance=models.CharField(max_length=50,null=True)
    user=models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    vehicle=models.ForeignKey(tbl_vehicle,on_delete=models.CASCADE)
    booking_fromdate=models.DateField(null=True)
    booking_todate=models.DateField()
    fromlocalplace=models.ForeignKey(tbl_localplace, on_delete=models.CASCADE,related_name="from_place",null=True)
    tolocalplace=models.ForeignKey(tbl_localplace, on_delete=models.CASCADE,related_name="to_place",null=True)

class tbl_complaints(models.Model):
    complaint_title=models.CharField(max_length=50)
    complaint_content=models.CharField(max_length=50)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=50,null=True)
    complaint_status=models.IntegerField(default=0)
    user=models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    booking=models.ForeignKey(tbl_booking, on_delete=models.CASCADE)
    
    