from django.urls import path
from mystudentsapp import views

urlpatterns = [
    path('my-students/',views.mystudents,name="mystudents"),       
]
