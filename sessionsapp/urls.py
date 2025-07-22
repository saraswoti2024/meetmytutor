from django.urls import path
from sessionsapp import views

urlpatterns = [
    path('tutor_session/',views.tutor_session,name="tutor_session"),       
]
