from django.shortcuts import render,redirect
from Admin.models import *
from Driver.models import *
from User.models import *
from Guest.models import *
from datetime import datetime

# Create your views here.
def Profile(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        profiledata=tbl_user.objects.get(id=request.session['uid'])
        return render(request,"User/Profile.html",{'Data':profiledata})
def ChangePassword(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        profiledata=tbl_user.objects.get(id=request.session['uid'])
        dbpass=profiledata.user_password
        if request.method=="POST":
            old=request.POST.get('txt_oldpassword')
            new=request.POST.get('txt_newpassword')
            confirm=request.POST.get('txt_repassword')
            if old==dbpass:
                if new==confirm:
                    profiledata.user_password=new
                    profiledata.save()
                    return render(request,"User/ChangePassword.html",{'msg':'Password changed'})
                else:
                    return render(request,"User/ChangePassword.html",{'msg':'New password mismatch'})
            else:
                return render(request,"User/ChangePassword.html",{'msg':'old password incorrect'})
        else:
            return render(request,"User/ChangePassword.html",{'Data':profiledata})
def EditProfile(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        profiledata=tbl_user.objects.get(id=request.session['uid'])
        if request.method=="POST":
            name=request.POST.get('txt_name')
            email=request.POST.get('txt_email')
            contact=request.POST.get('txt_contact')
            address=request.POST.get('txt_address')
            profiledata.user_name=name
            profiledata.user_email=email
            profiledata.user_contact=contact
            profiledata.user_address=address
            profiledata.save()
            return render(request,"User/EditProfile.html",{'msg':'Updated'})
        else:
            return render(request,"User/EditProfile.html",{'Data':profiledata})
def HomePage(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        # print(request.session['uid'])
        userdata=tbl_user.objects.get(id=request.session['uid'])
        return render(request,"User/HomePage.html",{'Data':userdata})
def Complaint(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        complaintdata=tbl_complaint.objects.filter(user=request.session['uid'])
        userdata=tbl_user.objects.get(id=request.session['uid'])
        if request.method=="POST":
            title=request.POST.get("txt_title")
            content=request.POST.get("txt_content")
            tbl_complaint.objects.create(complaint_title=title,complaint_content=content,user=userdata)
            return render(request,"User/Complaint.html",{'msg':"Data inserted"})
        else:
            return render(request,"User/Complaint.html",{'complaintdata':complaintdata})
def complaintdelete(request,cid):
    tbl_complaint.objects.get(id=cid).delete()
    return redirect("User:Complaint")
# def Viewvehicle(request):
#     if "uid" not in request.session:
#         return redirect("Guest:Login")
#     else:
#         userdata = tbl_user.objects.get(id=request.session['uid'])
#         vehicle_type = request.GET.get('vehicletype')  # dropdown value
#         if vehicle_type:
#             vehicledata = tbl_vehicle.objects.filter(vehicle_type=vehicle_type)
#         else:
#             vehicledata = tbl_vehicle.objects.all()
#         return render(request,"User/Viewvehicle.html",{'Data': userdata,'vehicledata': vehicledata,'selected_type': vehicle_type})
def Viewvehicle(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        seltype=tbl_vehicletype.objects.all()
        vehicledata=tbl_vehicle.objects.all()
        userdata=tbl_user.objects.get(id=request.session['uid'])
        return render(request,"User/Viewvehicle.html",{'seltype':seltype,'Data':userdata,'vehicledata':vehicledata})

def Ajaxvehicletype(request):
    tid=request.GET.get('did')
    vehicledata=tbl_vehicle.objects.filter(vehicletype=tid)
    return render(request,'User/Ajaxvehicletype.html',{'data':vehicledata})

# def Booking(request,vid):
#     if "uid" not in request.session:
#         return redirect("Guest:Login")
#     else:
#         userdata=tbl_user.objects.get(id=request.session['uid'])
#         districtdata=tbl_district.objects.all()
#         placedata=tbl_place.objects.all()
#         localplacedata=tbl_localplace.objects.all()
#         bookingdata=tbl_booking.objects.all()
#         vechicledata=tbl_vehicle.objects.all()
#         if request.method=="POST":
#             fromdate=request.POST.get("txt_fromdate")
#             date=request.POST.get("txt_todate")
#             fromlocalplace=tbl_localplace.objects.get(id=request.POST.get("from_localplace"))
#             tolocalplace=tbl_localplace.objects.get(id=request.POST.get("to_localplace"))
#             vechicledata=tbl_vehicle.objects.get(id=vid)
#             tbl_booking.objects.create(booking_fromdate=fromdate,booking_todate=date,fromlocalplace=fromlocalplace,tolocalplace=tolocalplace,user=userdata,vehicle=vechicledata)
#             return render(request,"User/Booking.html",{'msg':"Data Inserted"})
#         else:
#             return render(request,"User/Booking.html",{'districtdata':districtdata,'placedata':placedata,'localplacedata':localplacedata,'bookingdata':bookingdata,'vehicledata':vechicledata})

def Booking(request, vid):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        userdata = tbl_user.objects.get(id=request.session['uid'])
        bookingdata = tbl_booking.objects.all()
        vehicledata = tbl_vehicle.objects.all()

        if request.method == "POST":

            booktype = request.POST.get("sel_booktype")
            fromdate = request.POST.get("txt_fromdate")
            todate = request.POST.get("txt_todate")
            vehicle = tbl_vehicle.objects.get(id=vid)

            #location name from map
            from_place = request.POST.get("from_place")
            to_place = request.POST.get("to_place")

            # Convert to date object
            from_date_obj = datetime.strptime(fromdate, "%Y-%m-%d").date()

            if booktype == "single":
                booking_fromdate = from_date_obj
                booking_todate = from_date_obj
                total_days = 1
            else:
                to_date_obj = datetime.strptime(todate, "%Y-%m-%d").date()
                booking_fromdate = from_date_obj
                booking_todate = to_date_obj
                total_days = (to_date_obj - from_date_obj).days + 1

            # Prevent wrong date
            if total_days <= 0:
                return render(request, "User/Booking.html", {
                    'msg': "Invalid Date Selection"
                })

            # Calculate Total Amount
            distance = float(request.POST.get("distance_km"))
            total_amount = (total_days * vehicle.vehicle_baseprice) + (distance * vehicle.vehicle_kmprice)
            print(total_amount)

            # Calculate Advance Price
            advance = total_amount * 0.20
            balance = int(total_amount - advance)

            tbl_booking.objects.create(
                booking_fromdate=booking_fromdate,
                booking_todate=booking_todate,
                booking_fromplace=from_place,
                booking_toplace=to_place, 
                booking_days=total_days,
                booking_amount=total_amount,
                booking_advance=advance,
                booking_distance=distance,
                user=userdata,
                vehicle=vehicle
            )

            return render(request, "User/Payment.html", {
                'msg': f"Booking Successful! Total Amount: ₹{total_amount}"
            })

        else:
            return render(request, "User/Booking.html", {
                'bookingdata': bookingdata,
                'vehicledata': vehicledata
            })



def ajaxbookingtype(request):
    return render(request,'User/ajaxbookingtype.html')

def Ajaxlocalplace(request):
    place_id = request.GET.get('did')
    localplacedata = tbl_localplace.objects.filter(place_id=place_id)
    return render(request, "User/Ajaxlocalplace.html", {'localplacedata': localplacedata})

def MyBooking(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        bookingdata=tbl_booking.objects.filter(user=request.session['uid'])
        userdata=tbl_user.objects.get(id=request.session['uid'])
        return render(request,"User/MyBooking.html",{'Data':userdata,'bookingdata':bookingdata})


def Payment(request, bid):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        userdata = tbl_user.objects.get(id=request.session['uid'])
        bookingdata = tbl_booking.objects.get(id=bid, user=userdata)
        advance=int(bookingdata.booking_advance)

        if request.method == "POST":
            bookingdata.bookinguser_status = 3   
            bookingdata.save()
            return render(request, "User/Payment.html", {'msg': 'Payment Successful'})
        else:
            return render(request, "User/Payment.html", {'bookingdata': bookingdata,'advance':advance})   
        
def Paymentfull(request, bid):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        userdata = tbl_user.objects.get(id=request.session['uid'])
        bookingdata = tbl_booking.objects.get(id=bid, user=userdata)
        total=int(bookingdata.booking_amount)
        advance=int(bookingdata.booking_advance)
        bal=total-advance
        if request.method == "POST":
            bookingdata.bookinguser_status = 5   
            bookingdata.save()
            return render(request, "User/Payment.html", {'msg': 'Full Payment Successful'})
        else:
            return render(request, "User/Payment.html", {'bookingdata': bookingdata,'bal':bal})   
        

def Complaints(request, bid):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        userdata = tbl_user.objects.get(id=request.session['uid'])
        booking = tbl_booking.objects.get(id=bid, user=userdata)
        complaintdata = tbl_complaints.objects.filter(user=userdata, booking=booking)
        if request.method == "POST":
            title = request.POST.get("txt_title")
            content = request.POST.get("txt_content")
            tbl_complaints.objects.create(complaint_title=title,complaint_content=content,user=userdata,booking=booking)
            booking.bookinguser_status = 6
            booking.save()
            return redirect("User:MyBooking")
            #return render(request, "User/Complaints.html", {'msg': "Complaint submitted successfully",'booking': booking,'complaintdata': complaintdata})
        else:
            return render(request, "User/Complaints.html", {'booking': booking,'complaintdata': complaintdata})
def complaintdelete(request,csid):
    tbl_complaints.objects.get(id=csid).delete()
    return redirect("User:Complaints") 
def MyComplaints(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        userdata = tbl_user.objects.get(id=request.session['uid'])
        complaintdata = tbl_complaints.objects.filter(user=userdata)
        return render(request, "User/MyComplaints.html", {'complaintdata': complaintdata})
def Logout(request):
    del request.session["uid"]
    return redirect("Guest:Login")
def UserAccept(request,aubid):
    booking = tbl_booking.objects.get(id=aubid)
    booking.bookinguser_status = 1
    booking.save()
    return redirect('User:MyBooking')

def UserReject(request,rubid):
    booking = tbl_booking.objects.get(id=rubid)
    booking.bookinguser_status = 2
    booking.save()
    return redirect('User:MyBooking')

# def comadd(request, bid):
#     booking = tbl_booking.objects.get(id=bid)
#     booking.bookinguser_status = 6
#     booking.save()
#     return redirect("User:MyBooking")


    
