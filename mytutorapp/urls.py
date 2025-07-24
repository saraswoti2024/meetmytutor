from django.urls import path
from mytutorapp import views

urlpatterns = [
     path('my_tutors/',views.my_tutors_view,name="my_tutors"), 
     path('ongoing_sessions/',views.mytutors_ongoing,name="my_tutors_ongoing"), 
     path('complete_sessions/',views.mytutors_complete,name="my_tutors_complete"), 
]

  