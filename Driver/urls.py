from django.urls import path
from Driver import views
app_name="Driver"
urlpatterns = [
    path('DriverHomePage/',views.DriverHomePage ,name="DriverHomePage"),
    path('MyProfile/',views.MyProfile ,name="MyProfile"),
    path('EditProfile/',views.EditProfile ,name="EditProfile"),
    path('ChangePassword/',views.ChangePassword ,name="ChangePassword"),
    path('Brand/',views.Brand ,name="Brand"),
    path('deleBrand/<int:dbid>',views.deleBrand,name="deleBrand"),
    path('Model/',views.Model ,name="Model"),
    path('editmodel/<int:emid>',views.editmodel,name="editmodel"),
    path('delmodel/<int:dmid>',views.delmodel,name="delmodel"),
    path('Vehicle/',views.Vehicle ,name="Vehicle"),
    path('Ajaxmodel/',views.Ajaxmodel,name='Ajaxmodel'),
    path('delvehicle/<int:dvlid>',views.delvehicle,name="delvehicle"),
    path('Requestview/',views.Requestview,name="Requestview"),
    path('acceptbookingdata/<int:abid>/',views.acceptbookingdata,name="acceptbookingdata"),
    path('rejectbookingdata/<int:rbid>/',views.rejectbookingdata,name="rejectbookingdata"),
    #path('Amount/',views.Amount ,name="Amount"),
    path('Amount/<int:bid>/', views.Amount, name="Amount"),
    path('reqfullamt/<int:bid>/', views.reqfullamt, name="reqfullamt"),
    path('Logout/',views.Logout,name="Logout"),

]
 