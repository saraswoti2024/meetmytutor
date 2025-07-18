from django.urls import path
from findtutor import views

urlpatterns = [
    path('all-tutor/',views.all_tutor,name="all_tutor"),       
]
