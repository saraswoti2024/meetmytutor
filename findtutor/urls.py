from django.urls import path
from findtutor import views

urlpatterns = [
    path('all-tutor/',views.all_tutor_view,name="all_tutor"),       
    path('nearby-tutor/',views.nearby_tutor_view,name="nearby_tutor"),       
    path('view_profile/<int:id>',views.view_tutor_profile_view,name="view_tutor_profile"),       
]
