from django.urls import path
from accounts import views
urlpatterns = [
    path('student_register/',views.student_register,name="student_register"),    
]
