from django.urls import path
from requestapp import views

urlpatterns = [
    path('tutor_session/<int:id>',views.tutor_session_request,name="tutor_session_request"),       
    path('request_list/',views.request_list,name="request_list"),       
]
