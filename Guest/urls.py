from django.urls import path
from Guest import views
app_name="Guest"
urlpatterns = [
    path('NewUser/',views.NewUser ,name="NewUser"),
    path('AjaxPlace/',views.AjaxPlace,name='AjaxPlace'),
    path('Login/',views.Login ,name="Login"),
    path('NewSeller/',views.NewSeller ,name="NewSeller"),
    path('DriverRegistration/',views.DriverRegistration ,name="DriverRegistration"),
     path('Index/',views.Index ,name="Index"),
]