from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from Driver.models import *
# Create your views here.
def NewUser(request):
    districtdata=tbl_district.objects.all()
    placedata=tbl_place.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_name")
        gender=request.POST.get("txt_gender")
        contact=request.POST.get("txt_contact")
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_password")
        placee=tbl_place.objects.get(id=request.POST.get("sel_place"))
        address=request.POST.get("txt_address") 
        photo=request.FILES.get("txt_photo")
        usercount=tbl_user.objects.filter(user_email=email).count()
        if usercount >0:
            return render(request,"Guest/NewUser.html",{'msg':"User Aready Exist"})
        else:
            tbl_user.objects.create(user_name=name,user_gender=gender,user_contact=contact,user_email=email,user_password=password,place=placee,user_address=address,user_photo=photo)
        return render(request,"Guest/NewUser.html",{'msg':"Data Inserted"})
    else:
        return render(request,"Guest/NewUser.html",{'districtdata':districtdata,'placedata':placedata})
def AjaxPlace(request):
    districtid=request.GET.get('did')
    placedata=tbl_place.objects.filter(district=districtid)
    return render(request,"Guest/AjaxPlace.html",{'placedata':placedata})
def Login(request):
    if request.method=="POST":
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_password")
        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
        admincount=tbl_adminregistration.objects.filter(admin_email=email,admin_password=password).count()
        sellercount=tbl_seller.objects.filter(seller_email=email,seller_password=password).count()
        drivercount=tbl_driver.objects.filter(driver_email=email,driver_password=password).count()
        if usercount >0:
            userdata=tbl_user.objects.get(user_email=email,user_password=password)
            request.session['uid']=userdata.id
            return redirect("User:HomePage")
        elif admincount >0:
            admindata=tbl_adminregistration.objects.get(admin_email=email,admin_password=password)
            request.session['aid']=admindata.id
            return redirect("Admin:AdminHomePage")
        elif sellercount >0:
            sellerdata=tbl_seller.objects.get(seller_email=email,seller_password=password)
            request.session['sid']=sellerdata.id
            return redirect("Seller:SellerHomePage") 
        elif drivercount >0:
            driverdata=tbl_driver.objects.get(driver_email=email,driver_password=password)
            request.session['drid']=driverdata.id
            return redirect("Driver:DriverHomePage") 
        else:
            return render(request,"Guest/Login.html",{'msg':'invalidlogin'})
    else:
       return render(request,"Guest/Login.html") 
def NewSeller(request):
    districtdata=tbl_district.objects.all()
    placedata=tbl_place.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_name")
        contact=request.POST.get("txt_contact")
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_password")
        placee=tbl_place.objects.get(id=request.POST.get("sel_place"))
        establishdate=request.POST.get("txt_estdate")
        licenseno=request.POST.get("txt_licenseno") 
        owner=request.POST.get("txt_owner") 
        licenseproof=request.FILES.get("txt_licenseproof")
        ownerproof=request.FILES.get("txt_ownerproof")
        tbl_seller.objects.create(seller_name=name,seller_contact=contact,seller_email=email,seller_password=password,place=placee,seller_establishdate=establishdate,seller_licenseno=licenseno,seller_ownername=owner,seller_licenseproof=licenseproof, seller_ownerproof=ownerproof)
        return render(request,"Guest/NewSeller.html",{'msg':"Data Inserted"})
    else:
        return render(request,"Guest/NewSeller.html",{'districtdata':districtdata,'placedata':placedata})

def DriverRegistration(request):
    districtdata=tbl_district.objects.all()
    placedata=tbl_place.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address") 
        photo=request.FILES.get("txt_photo")
        license=request.FILES.get("txt_license")
        password=request.POST.get("txt_password")
        placee=tbl_place.objects.get(id=request.POST.get("sel_place"))
        drivercount=tbl_driver.objects.filter(driver_email=email).count()
        if drivercount >0:
            return render(request,"Guest/DriverRegistration.html",{'msg':"Driver Aready Exist"})
        else:
            tbl_driver.objects.create(driver_name=name,driver_email=email,driver_contact=contact,driver_address=address,driver_photo=photo,driver_license=license,driver_password=password,place=placee)
        return render(request,"Guest/DriverRegistration.html",{'msg':"Data Inserted"})
    else:
        return render(request,"Guest/DriverRegistration.html",{'districtdata':districtdata,'placedata':placedata})

def Index(request):
    
    return render(request,"Guest/Index.html")
    