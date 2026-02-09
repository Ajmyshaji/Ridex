from django.urls import path
from Admin import views
from User import views
app_name="User"
urlpatterns = [
   
    path('Profile/',views.Profile ,name="Profile"),
    path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('HomePage/',views.HomePage ,name="HomePage"),
    path('Complaint/',views.Complaint ,name="Complaint"),
    path('complaintdelete/<int:cid>',views.complaintdelete,name="complaintdelete"),
    path('Viewvehicle/',views.Viewvehicle ,name="Viewvehicle"),
    path('Booking/<int:vid>',views.Booking ,name="Booking"),
    path('Ajaxlocalplace/',views.Ajaxlocalplace,name='Ajaxlocalplace'),
    path('MyBooking/',views.MyBooking,name='MyBooking'),
    path('ajaxbookingtype/',views.ajaxbookingtype,name="ajaxbookingtype"),
    path('Payment/<int:bid>/', views.Payment, name='Payment'),
    path('Complaints/<int:bid>/', views.Complaints, name="Complaints"),
    path('MyComplaints/', views.MyComplaints, name="MyComplaints"),
    path('complaintdelete/<int:csid>/', views.complaintdelete, name="complaintdelete"),
    path('Logout/', views.Logout, name="Logout"),
    path('UserAccept/<int:aubid>/',views.UserAccept,name="UserAccept"),
    path('UserReject/<int:rubid>/',views.UserReject,name="UserReject"),
    path('Ajaxvehicletype/',views.Ajaxvehicletype,name="Ajaxvehicletype"),

]

