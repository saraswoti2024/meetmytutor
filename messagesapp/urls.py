from django.urls import path
from messagesapp import views

urlpatterns = [
    path('view-message-tutor/',views.message_view_tutor,name="messages_tutor"),              
    path('view-message-student/',views.message_view_student,name="messages_student"),              
]
