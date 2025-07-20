from django.shortcuts import render

# Create your views here.
def tutor_session_request(request):
    return render(request,'request_session/request_tutor.html')
