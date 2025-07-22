from django.shortcuts import render
from profileapp.models import *
from requestapp.models import Requesting_tutor
# Create your views here.
def mystudents(request):
    tutor = Profile_Tutor.objects.get(user=request.user)
    data = Requesting_tutor.objects.filter(status='accepted',tutor_user=tutor)
    context = {
        'data' : data
    }
    return render(request,'student/tutor_students.html',context)