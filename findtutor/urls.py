from django.urls import path
from findtutor import views

urlpatterns = [
    path('all-tutor/',views.all_tutor_view,name="all_tutor"),       
]
