from django.shortcuts import render,redirect
from Admin.models import *
from Driver.models import *
from User.models import *
from Guest.models import *
# Create your views here.
def MyProfile(request):
    if "drid" not in request.session:
        return redirect("Guest:Login")
    else:
        profiledata=tbl_driver.objects.get(id=request.session['drid'])
        return render(request,"Driver/MyProfile.html",{'Data':profiledata})
def ChangePassword(request):
    if "drid" not in request.session:
        return redirect("Guest:Login")
    else:
        profiledata=tbl_driver.objects.get(id=request.session['drid'])
        dbpass=profiledata.driver_password
        if request.method=="POST":
            old=request.POST.get('txt_oldpassword')
            new=request.POST.get('txt_newpassword')
            confirm=request.POST.get('txt_repassword')
            if old==dbpass:
                if new==confirm:
                    profiledata.driver_password=new
                    profiledata.save()
                    return render(request,"Driver/ChangePassword.html",{'msg':'Password changed'})
                else:
                    return render(request,"Driver/ChangePassword.html",{'msg':'New password mismatch'})
            else:
                return render(request,"Driver/ChangePassword.html",{'msg':'old password incorrect'})
        else:
            return render(request,"Driver/ChangePassword.html",{'Data':profiledata})
def EditProfile(request):
    if "drid" not in request.session:
        return redirect("Guest:Login")
    else:
        profiledata=tbl_driver.objects.get(id=request.session['drid'])
        if request.method=="POST":
            name=request.POST.get('txt_name')
            email=request.POST.get('txt_email')
            contact=request.POST.get('txt_contact')
            address=request.POST.get('txt_address')
            photo=request.FILES.get("txt_photo")
            profiledata.driver_name=name
            profiledata.driver_email=email
            profiledata.driver_contact=contact
            profiledata.driver_address=address
            if photo:
                profiledata.driver_photo=photo
        
            profiledata.save()
            return render(request,"Driver/EditProfile.html",{'msg':'Updated'})
        else:
            return render(request,"Driver/EditProfile.html",{'Data':profiledata})
def DriverHomePage(request):
    if "drid" not in request.session:
        return redirect("Guest:Login")
    else:
        # print(request.session['uid'])
        driverdata=tbl_driver.objects.get(id=request.session['drid'])
        return render(request,"Driver/DriverHomePage.html",{'Data':driverdata})
def Vehicle(request):
    if "drid" not in request.session:
        return redirect("Guest:Login")
    else:
        driverdata=tbl_driver.objects.get(id=request.session['drid'])
        vehicledata=tbl_vehicle.objects.filter(driver=request.session['drid'])
        vehicletypedata=tbl_vehicletype.objects.all()
        branddata=tbl_brand.objects.all()
        modeldata=tbl_model.objects.all()
        if request.method=="POST":
            name=request.POST.get("txt_name")
            details=request.POST.get("txt_details")
            photo=request.FILES.get("txt_photo")
            modell=tbl_model.objects.get(id=request.POST.get("sel_model"))
            vehicletype=tbl_vehicletype.objects.get(id=request.POST.get("sel_vehicle"))
            baseprice=request.POST.get("txt_baseprice")
            kmprice=request.POST.get("txt_kmprice")
            capasity=request.POST.get("txt_capasity")
            tbl_vehicle.objects.create(vehicle_name=name,vehicle_details=details,vehicle_photo=photo,vehicletype=vehicletype,vehicle_baseprice=baseprice,vehicle_kmprice=kmprice,vehicle_capasity=capasity,model=modell,driver=driverdata)
            return render(request,"Driver/Vehicle.html",{'msg':"Data Inserted"})
        else:
            return render(request,"Driver/Vehicle.html",{'vehicledata':vehicledata,'branddata':branddata,'modeldata':modeldata,'vehicletypedata':vehicletypedata})
def Ajaxmodel(request):
    brandid=request.GET.get('did')
    modeldata=tbl_model.objects.filter(brand=brandid)
    return render(request,"Driver/Ajaxmodel.html",{'modeldata':modeldata})
def delvehicle(request,dvlid):
    tbl_vehicle.objects.get(id=dvlid).delete()
    return redirect("Driver:Vehicle")
def Requestview(request):
    if "drid" not in request.session:
        return redirect("Guest:Login")
    else:
        driverdata=tbl_driver.objects.get(id=request.session['drid'])
        # vehicledata=tbl_vehicle.objects.filter(driver=request.session['drid'])
        bookingdata = tbl_booking.objects.filter(vehicle__driver=driverdata)
        acceptbookingdata=tbl_booking.objects.filter(booking_status=1)
        rejectbookingdata=tbl_booking.objects.filter(booking_status=2)
        return render(request,"Driver/Requestview.html",{'bookingdata': bookingdata,'driverdata':driverdata,'acceptbookingdata':acceptbookingdata,'rejectbookingdata':rejectbookingdata})
def acceptbookingdata(request,abid):
    data=tbl_booking.objects.get(id=abid)
    data.booking_status=1
    data.save()
    return render(request,"Driver/Requestview.html",{'msg':'accepted'})


def rejectbookingdata(request,rbid):
    data=tbl_booking.objects.get(id=rbid)
    data.booking_status=2
    data.save()
    return render(request,"Driver/Requestview.html",{'msg':'rejected'})

def reqfullamt(request,bid):
    data=tbl_booking.objects.get(id=bid)
    data.bookinguser_status=4
    data.save()
    return render(request,"Driver/Requestview.html",{'msg':'Requested Full Payment'})

# def Amount(request):
#     driverdata=tbl_driver.objects.get(id=request.session['drid'])
#     bookingdata = tbl_booking.objects.filter(vehicle__driver=driverdata)
#     if request.method=="POST":
#         amount=request.POST.get("txt_amount")
#         bookingdata.booking_amount = amount
#         bookingdata.save()
#         return render(request,"Driver/Requestview.html",{'msg':"Data updated"})
#     else:
#         return render(request,"Driver/Amount.html",{'bookingdata': bookingdata,'driverdata':driverdata})
    
def Amount(request, bid):
    if "drid" not in request.session:
        return redirect("Guest:Login")
    else:
        driverdata = tbl_driver.objects.get(id=request.session['drid'])
        bookingdata = tbl_booking.objects.get(id=bid, vehicle__driver=driverdata)

        if request.method == "POST":
            amount = request.POST.get("txt_amount")
            bookingdata.booking_amount = amount
            bookingdata.save()
            return render(request, "Driver/Requestview.html", {'msg': "Amount added successfully"})

        else:
            return render(request, "Driver/Amount.html", {'bookingdata': bookingdata,'driverdata': driverdata})

def Logout(request):
    del request.session["drid"]
    return redirect("Guest:Login")

