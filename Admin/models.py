from django.db import models

# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)
class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)
class tbl_adminregistration(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_email=models.CharField(max_length=50)
    admin_password=models.CharField(max_length=50)
class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)
class tbl_subcategory(models.Model):
    subcategory_name=models.CharField(max_length=50)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)
class tbl_department(models.Model):
    department_name=models.CharField(max_length=50)
class tbl_designation(models.Model):
    designation_name=models.CharField(max_length=50)
class tbl_employee(models.Model):
    employee_name=models.CharField(max_length=50)
    employee_gender=models.CharField(max_length=10)
    employee_contact=models.CharField(max_length=15)
    employee_doj=models.DateField(max_length=12)
    department=models.ForeignKey(tbl_department,on_delete=models.CASCADE)
    designation=models.ForeignKey(tbl_designation,on_delete=models.CASCADE)
    employee_salary=models.IntegerField()
class tbl_vehicletype(models.Model):
    vehicletype_name=models.CharField(max_length=50)
class tbl_brand(models.Model):
    brand_name=models.CharField(max_length=50)
class tbl_model(models.Model):
    model_name=models.CharField(max_length=50)
    brand=models.ForeignKey(tbl_brand,on_delete=models.CASCADE)
    
class tbl_localplace(models.Model):
    localplace_name=models.CharField(max_length=50)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    
    
    