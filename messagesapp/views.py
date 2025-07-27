from django.shortcuts import render

# Create your views here.
def message_view_tutor(request):
    return render(request,'messages/message_tutor.html')

def message_view_student(request):
    return render(request,'messages/message_student.html')