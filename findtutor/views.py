from django.shortcuts import render
from profileapp.models import Profile_Tutor
# Create your views here.
def all_tutor(request):
    all_tutors = Profile_Tutor.objects.all()
    context = {
        'all_tutors' : all_tutors
    }
    return render(request,'findtutor/all_tutor.html',context)