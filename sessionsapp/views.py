from django.shortcuts import render
from profileapp.models import *
from requestapp.models import *
# Create your views here.
def tutor_session(request):
    tutor = Profile_Tutor.objects.get(user=request.user)
    if tutor:
        list_req_tutor = Requesting_tutor.objects.filter(status='accepted',tutor_user=tutor)
    context = {
        'req_list' : list_req_tutor,
    } 
    return render(request,'sessions_temp/tutor_sessions.html',context)