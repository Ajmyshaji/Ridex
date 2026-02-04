from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
# Create your views here.
def District(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        admindata=tbl_adminregistration.objects.get(id=request.session['aid'])
        districtdata=tbl_district.objects.all()
        if request.method=="POST":
            district=request.POST.get("txt_district")
            districtcount=tbl_district.objects.filter(district_name=district).count()
            if districtcount >0:
                return render(request,"Admin/District.html",{'msg':"District Aready Exist"})
            else:
                tbl_district.objects.create(district_name=district)
            return render(request,"Admin/District.html",{'msg':"Data Inserted"})
        else:
            return render(request,"Admin/District.html",{'Data':admindata,'districtdata':districtdata})
def Category(request):
    categorydata=tbl_category.objects.all()
    if request.method=="POST":
        category=request.POST.get("txt_category")
        categorycount=tbl_category.objects.filter(category_name=category).count()
        if categorycount >0:
            return render(request,"Admin/Category.html",{'msg':"Categort Aready Exist"})
        else:
            tbl_category.objects.create(category_name=category)
        return render(request,"Admin/Category.html")
    else:
        return render(request,"Admin/Category.html",{'categorydata': categorydata})
def AdminRegistration(request):
    regdata=tbl_adminregistration.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_password")
        admincount=tbl_adminregistration.objects.filter(admin_email=email).count()
        if admincount >0:
            return render(request,"Admin/AdminRegistration.html",{'msg':"Email Aready exist"})
        else:
            tbl_adminregistration.objects.create(admin_name=name,admin_email=email,admin_password=password)
        return render(request,"Admin/AdminRegistration.html",{'msg':"Data Inserted"})
    else:
        return render(request,"Admin/AdminRegistration.html",{'regdata': regdata})
def deldistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("Admin:District")
def delcategory(request,cid):
    tbl_category.objects.get(id=cid).delete()
    return redirect("Admin:Category")
def delregistration(request,rid):
    tbl_adminregistration.objects.get(id=rid).delete()
    return redirect("Admin:AdminRegistration")
def editdistrict(request,did):
    editdata=tbl_district.objects.get(id=did)
    if request.method=="POST":
        district=request.POST.get("txt_district")
        editdata.district_name=district
        editdata.save()
        return redirect("Admin:District")
    else:
        return render(request,"Admin/District.html/",{'editdata':editdata})
def editcategory(request,cid):
    editdata=tbl_category.objects.get(id=cid)
    if request.method=="POST":
        category=request.POST.get("txt_category")
        editdata.category_name=category
        editdata.save()
        return redirect("Admin:Category")
    else:
        return render(request,"Admin/Category.html/",{'editdata':editdata})

def editregistration(request,rid):
    editdata=tbl_adminregistration.objects.get(id=rid)
    if request.method=="POST":
        # registration=request.POST.get("txt_name","txt_email","txt_password")
        adminname=request.POST.get("txt_name")
        adminemail=request.POST.get("txt_email")
        adminpassword=request.POST.get("txt_password")
        editdata.admin_name=adminname
        editdata.admin_email= adminemail
        editdata.admin_password=adminpassword
        editdata.save()
        return redirect("Admin:AdminRegistration")
    else:
        return render(request,"Admin/AdminRegistration.html/",{'editdata':editdata})
def Place(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        admindata=tbl_adminregistration.objects.get(id=request.session['aid'])
        districtdata=tbl_district.objects.all()
        placedata=tbl_place.objects.all()
        if request.method=="POST":
            place=request.POST.get("txt_place")
            districtname=tbl_district.objects.get(id=request.POST.get("sel_district"))
            placecount=tbl_place.objects.filter(place_name=place).count()
            if placecount >0:
                return render(request,"Admin/Place.html",{'msg':"Place Aready Exist"})
            else:
                tbl_place.objects.create(place_name=place,district=districtname)
            return render(request,"Admin/Place.html",{'msg':"Data Inserted"})
        else:
            return render(request,"Admin/Place.html",{'Data':admindata,'districtdata':districtdata,'placedata':placedata})
def editplace(request,pid):
    districtdata=tbl_district.objects.all()
    editdata=tbl_place.objects.get(id=pid)
    if request.method=="POST":
        place=request.POST.get("txt_place")
        districtname=tbl_district.objects.get(id=request.POST.get("sel_district"))
        editdata.place_name=place
        editdata.district=districtname
        editdata.save()
        return redirect("Admin:Place")
    else:
        return render(request,"Admin/Place.html/",{'districtdata':districtdata,'editdata':editdata})
def delplace(request,pid):
    tbl_place.objects.get(id=pid).delete()
    return redirect("Admin:Place")
def SubCategory(request):
    categorydata=tbl_category.objects.all()
    subcategorydata=tbl_subcategory.objects.all()
    if request.method=="POST":
        subcat=request.POST.get("txt_subcategory")
        catname=tbl_category.objects.get(id=request.POST.get("sel_category"))
        subcategorycount=tbl_subcategory.objects.filter(subcategory_name=subcat).count()
        if subcategorycount >0:
            return render(request,"Admin/SubCategory.html",{'msg':"Subcategory Aready Exist"})
        else:
            tbl_subcategory.objects.create(subcategory_name=subcat,category=catname)
        return render(request,"Admin/SubCategory.html",{'msg':"Data Inserted"})
    else:
        return render(request,"Admin/SubCategory.html",{'categorydata':categorydata,'subcategorydata':subcategorydata})
def editSubCategory(request,sid):
    categorydata=tbl_category.objects.all()
    editdata=tbl_subcategory.objects.get(id=sid)
    if request.method=="POST":
        subcat=request.POST.get("txt_subcategory")
        categoryname=tbl_category.objects.get(id=request.POST.get("sel_category"))
        editdata.subcategory_name=subcat
        editdata.category=categoryname
        editdata.save()
        return redirect("Admin:SubCategory")
    else:
        return render(request,"Admin/SubCategory.html/",{'categorydata':categorydata,'editdata':editdata})
def deleteSubCategory(request,sid):
    tbl_subcategory.objects.get(id=sid).delete()
    return redirect("Admin:SubCategory")
def Department(request):
    departmentdata=tbl_department.objects.all()
    if request.method=="POST":
        department=request.POST.get("txt_department")
        departmentcount=tbl_department.objects.filter(department_name=department).count()
        if departmentcount >0:
            return render(request,"Admin/Department.html",{'msg':"Department Aready Exist"})
        else:
            tbl_department.objects.create(department_name=department)
        return render(request,"Admin/Department.html",{'msg':"Data Inserted"})
    else:
        return render(request,"Admin/Department.html",{'departmentdata':departmentdata})
def deletedepartment(request,deid):
    tbl_department.objects.get(id=deid).delete()
    return redirect("Admin:Department")
def editdepartment(request,deid):
    # departmentdata = tbl_department.objects.all()
    editdata=tbl_department.objects.get(id=deid)
    if request.method=="POST":
        department=request.POST.get("txt_department")
        editdata.department_name=department
        editdata.save()
        return redirect("Admin:Department")
    else:
        return render(request,"Admin/Department.html",{'editdata':editdata})
def Designation(request):
    designationdata=tbl_designation.objects.all()
    if request.method=="POST":
        designation=request.POST.get("txt_designation")
        tbl_designation.objects.create(designation_name=designation)
        return render(request,"Admin/Designation.html",{'msg':"Data Inserted"})
    else:
        return render(request,"Admin/Designation.html",{'designationdata':designationdata})
def deletedesignation(request,desid):
    tbl_designation.objects.get(id=desid).delete()
    return redirect("Admin:Designation")
def editdesignation(request,desid):
    # designationdata=tbl_designation.objects.all()
    editdata=tbl_designation.objects.get(id=desid)
    if request.method=="POST":
        designation=request.POST.get("txt_designation")
        editdata.designation_name=designation
        editdata.save()
        return redirect("Admin:Designation")
    else:
        return render(request,"Admin/Designation.html",{'editdata':editdata})

def Employee(request):
    departmentdata=tbl_department.objects.all()
    designationdata=tbl_designation.objects.all()
    employeedata=tbl_employee.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_name")
        gender=request.POST.get("txt_gender")
        contact=request.POST.get("txt_contact")
        doj=request.POST.get("txt_doj")
        depname=tbl_department.objects.get(id=request.POST.get("sel_department"))
        desname=tbl_designation.objects.get(id=request.POST.get("sel_designation"))
        salary=request.POST.get("txt_salary")
        tbl_employee.objects.create(employee_name=name,employee_gender=gender,employee_contact=contact,employee_doj=doj,department=depname,designation=desname,employee_salary=salary)
        return render(request,"Admin/Employee.html",{'msg':"Data Inserted"})
    else:
        return render(request,"Admin/Employee.html",{'employeedata':employeedata,'departmentdata':departmentdata,'designationdata':designationdata})
def editemployee(request,empid):
    departmentdata=tbl_department.objects.all()
    designationdata=tbl_designation.objects.all()
    editdata=tbl_employee.objects.get(id=empid)
    if request.method=="POST":
        name=request.POST.get("txt_name")
        gender=request.POST.get("txt_gender")
        contact=request.POST.get("txt_contact")
        doj=request.POST.get("txt_doj")
        departmentname=tbl_department.objects.get(id=request.POST.get("sel_department"))
        designationname=tbl_designation.objects.get(id=request.POST.get("sel_designation"))
        salary=request.POST.get("txt_salary")
        editdata.employee_name=name
        editdata.employee_gender=gender
        editdata.employee_contact=contact
        editdata.employee_doj=doj
        editdata.department=departmentname
        editdata.designation=designationname
        editdata.employee_salary=salary
        editdata.save()
        return redirect("Admin:Employee")
    else:
        return render(request,"Admin/Employee.html",{'departmentdata':departmentdata,'designationdata':designationdata,'editdata':editdata})
def deleteemployee(request,empid):
    tbl_employee.objects.get(id=empid).delete()
    return redirect("Admin:Employee")
def UserList(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        userdata=tbl_user.objects.all()
        # acceptusertdata=tbl_user.objects.filter(user_status=1)
        # rejectusertdata=tbl_user.objects.filter(user_status=2)
        return render(request,"Admin/UserList.html",{'userdata':userdata})
def SellerList(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        sellerdata=tbl_seller.objects.all()
        acceptdata=tbl_seller.objects.filter(seller_status=1)
        rejectdata=tbl_seller.objects.filter(seller_status=2)
        return render(request,"Admin/SellerList.html",{'sellerdata':sellerdata,'acceptdata':acceptdata,'rejectdata':rejectdata})
def acceptseller(request,aid):
    data=tbl_seller.objects.get(id=aid)
    data.seller_status=1
    data.save()
    return render(request,"Admin/SellerList.html",{'msg':'verified'})
def rejectseller(request,rid):
    data=tbl_seller.objects.get(id=rid)
    data.seller_status=2
    data.save()
    return render(request,"Admin/SellerList.html",{'msg':'rejected'})
# def acceptuser(request,auid):
#     data=tbl_user.objects.get(id=auid)
#     data.user_status=1
#     data.save()
#     return render(request,"Admin/UserList.html",{'msg':'verified'})
# def rejectuser(request,ruid):
#     data=tbl_user.objects.get(id=ruid)
#     data.user_status=2
#     data.save()
#     return render(request,"Admin/UserList.html",{'msg':'rejected'})
def AdminHomePage(request):
    # print(request.session['uid'])
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        admindata=tbl_adminregistration.objects.get(id=request.session['aid'])
        return render(request,"Admin/AdminHomePage.html",{'Data':admindata})
def ViewComplaint(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        viewcomplaintdata=tbl_complaint.objects.filter(complaint_status=0)
        replied=tbl_complaint.objects.filter(complaint_status=1)
        return render(request,"Admin/ViewComplaint.html",{'viewcomplaintdata':viewcomplaintdata,'replied':replied})
def Reply(request,cid):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        complaintdata=tbl_complaint.objects.get(id=cid)
        if request.method=="POST":
            reply=request.POST.get("txt_reply")
            complaintdata.complaint_replay=reply
            complaintdata.complaint_status=1
            complaintdata.save()
            return render(request,"Admin/Reply.html",{'msg':'Repiled'})
        else:
            return render(request,"Admin/Reply.html")
def VehicleType(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        admindata=tbl_adminregistration.objects.get(id=request.session['aid'])
        vehicletypedata=tbl_vehicletype.objects.all()
        if request.method=="POST":
            vehicletype=request.POST.get("txt_vehicletype")
            vehicletypecount=tbl_vehicletype.objects.filter(vehicletype_name=vehicletype).count()
            if vehicletypecount >0:
                return render(request,"Admin/VehicleType.html",{'msg':"VehicleType Aready Exist"})
            else:
                tbl_vehicletype.objects.create(vehicletype_name=vehicletype)
            return render(request,"Admin/VehicleType.html",{'msg':"Data Inserted"})
        else:
            return render(request,"Admin/vehicletype.html",{'Data':admindata,'vehicletypedata':vehicletypedata})
def delVehicleType(request,dvid):
    tbl_vehicletype.objects.get(id=dvid).delete()
    return redirect("Admin:VehicleType")
# def editVehicleType(request,evid):
#     editdata=tbl_vehicletype.objects.get(id=evid)
#     if request.method=="POST":
#         vehicletype=request.POST.get("txt_vehicletype")
#         editdata.vehicletype_name=vehicletype
#         editdata.save()
#         return redirect("Admin:VehicleType")
#     else:
#         return render(request,"Admin/vehicletype.html/",{'editdata':editdata})


def DriverVerification(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        admindata=tbl_adminregistration.objects.get(id=request.session['aid'])
        driverdata=tbl_driver.objects.filter(driver_status=0)
        acceptdriverdata=tbl_driver.objects.filter(driver_status=1)
        rejectdriverdata=tbl_driver.objects.filter(driver_status=2)
        return render(request,"Admin/DriverVerification.html",{'Data':admindata,'driverdata':driverdata,'acceptdriverdata':acceptdriverdata,'rejectdriverdata':rejectdriverdata})
def acceptdriver(request,adid):
    acceptdata=tbl_driver.objects.get(id=adid)
    acceptdata.driver_status=1
    acceptdata.save()
    return render(request,"Admin/DriverVerification.html",{'msg':'verified'})
def rejectdriver(request,rdid):
    rejectdata=tbl_driver.objects.get(id=rdid)
    rejectdata.driver_status=2
    rejectdata.save()
    return render(request,"Admin/DriverVerification.html",{'msg':'rejected'})
def Brand(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        admindata=tbl_adminregistration.objects.get(id=request.session['aid'])
        branddata=tbl_brand.objects.all()
        if request.method=="POST":
            brand=request.POST.get("txt_brand")
            brandcount=tbl_brand.objects.filter(brand_name=brand).count()
            if brandcount >0:
                return render(request,"Admin/Brand.html",{'msg':"Brand Aready Exist"})
            else:
                tbl_brand.objects.create(brand_name=brand)
            return render(request,"Admin/Brand.html",{'msg':"Data Inserted"})
        else:
            return render(request,"Admin/Brand.html",{'Data':admindata,'branddata':branddata})
def deleBrand(request,dbid):
    tbl_brand.objects.get(id=dbid).delete()
    return redirect("Admin:Brand")
def Model(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        admindata=tbl_adminregistration.objects.get(id=request.session['aid'])
        branddata=tbl_brand.objects.all()
        modeldata=tbl_model.objects.all()
        if request.method=="POST":
            model=request.POST.get("txt_model")
            brandname=tbl_brand.objects.get(id=request.POST.get("sel_brand"))
            modelcount=tbl_model.objects.filter(model_name=model).count()
            if modelcount >0:
                return render(request,"Admin/Model.html",{'msg':"Model Aready Exist"})
            else:
                tbl_model.objects.create(model_name=model,brand=brandname)
            return render(request,"Admin/Model.html",{'msg':"Data Inserted"})
        else:
            return render(request,"Admin/Model.html",{'Data':admindata,'branddata':branddata,'modeldata':modeldata})
def editmodel(request,emid):
    branddata=tbl_brand.objects.all()
    editdata=tbl_model.objects.get(id=emid)
    if request.method=="POST":
        model=request.POST.get("txt_model")
        brandname=tbl_brand.objects.get(id=request.POST.get("sel_brand"))
        editdata.model_name=model
        editdata.brand=brandname
        editdata.save()
        return redirect("Admin:Model")
    else:
        return render(request,"Admin/Model.html/",{'branddata':branddata,'editdata':editdata})
def delmodel(request,dmid):
    tbl_model.objects.get(id=dmid).delete()
    return redirect("Admin:Model")
def Ajaxplace(request):
    districtid=request.GET.get('did')
    placedata=tbl_place.objects.filter(district=districtid)
    return render(request,"Guest/AjaxPlace.html",{'placedata':placedata})
def LocalPlace(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        admindata=tbl_adminregistration.objects.get(id=request.session['aid'])
        districtdata=tbl_district.objects.all()
        placedata=tbl_place.objects.all()
        localplacedata=tbl_localplace.objects.all()
        if request.method=="POST":
            localplace=request.POST.get("txt_localplace")
            placename=tbl_place.objects.get(id=request.POST.get("sel_place"))
            localplacecount=tbl_localplace.objects.filter(localplace_name=localplace).count()
            if localplacecount >0:
                return render(request,"Admin/LocalPlace.html",{'msg':"LocalPlace Aready Exist"})
            else:
                tbl_localplace.objects.create(localplace_name=localplace,place=placename)
            return render(request,"Admin/LocalPlace.html",{'msg':"Data Inserted"})
        else:
            return render(request,"Admin/LocalPlace.html",{'Data':admindata,'districtdata':districtdata,'placedata':placedata,'localplacedata':localplacedata})
# def editlocalplace(request,elid):
#     districtdata=tbl_district.objects.all()
#     placedata=tbl_place.objects.all()
#     editdata=tbl_localplace.objects.get(id=elid)
#     if request.method=="POST":
#         localplace=request.POST.get("txt_localplace")
#         districtname=tbl_district.objects.get(id=request.POST.get("sel_district"))
#         placename=tbl_place.objects.get(id=request.POST.get("sel_place"))
#         editdata.localplace_name=localplace
#         editdata.district=districtname
#         editdata.place=placename
#         editdata.save()
#         return redirect("Admin:Place")
#     else:
#         return render(request,"Admin/Place.html/",{'districtdata':districtdata,'editdata':editdata})
def dellocalplace(request,dlid):
    tbl_localplace.objects.get(id=dlid).delete()
    return redirect("Admin:LocalPlace")
# def ViewComplaints(request):
#     complaintdata = tbl_complaints.objects.all().order_by('-complaint_date')
#     return render(request, "Admin/Complaints.html",{'complaintdata': complaintdata})


def ViewComplaints(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        admindata=tbl_adminregistration.objects.get(id=request.session['aid'])
        complaintdata=tbl_complaints.objects.filter(complaint_status=0)
        replied=tbl_complaints.objects.filter(complaint_status=2)
        return render(request,"Admin/ViewComplaints.html",{'Data':admindata,'complaintdata':complaintdata,'replied':replied})
def Reply(request,cid):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        complaintdata=tbl_complaints.objects.get(id=cid)
        if request.method=="POST":
            reply=request.POST.get("txt_reply")
            complaintdata.complaint_reply=reply
            complaintdata.complaint_status=2
            complaintdata.save()
            return render(request,"Admin/Reply.html",{'msg':'Repiled'})
        else:
            return render(request,"Admin/Reply.html")
    
def Logout(request):
    del request.session["aid"]
    return redirect("Guest:Login")


def blockdriver(request, id):
    driver = tbl_driver.objects.get(id=id)
    driver.driver_status=3
    driver.save()
    return redirect("Admin:ViewComplaints")
