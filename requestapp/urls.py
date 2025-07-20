from django.urls import path
from requestapp import views

urlpatterns = [
    path('tutor_session/',views.tutor_session_request,name="tutor_session_request"),       
]
