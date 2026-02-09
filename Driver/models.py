from django.db import models
from Admin.models import *
from Guest.models import *
from Driver.models import *
# Create your models here.

class tbl_vehicle(models.Model):
    vehicle_name=models.CharField(max_length=50)
    vehicle_details=models.CharField(max_length=30)
    vehicle_photo=models.FileField(upload_to='Assets/UserDocs/')
    model=models.ForeignKey(tbl_model,on_delete=models.CASCADE)
    vehicletype=models.ForeignKey(tbl_vehicletype,on_delete=models.CASCADE)
    vehicle_baseprice=models.IntegerField()
    vehicle_kmprice=models.IntegerField()
    vehicle_status=models.IntegerField(default=0)
    vehicle_capasity=models.IntegerField()
    driver=models.ForeignKey(tbl_driver,on_delete=models.CASCADE)
    
    