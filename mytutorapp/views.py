from django.shortcuts import render
from profileapp.models import *
from requestapp.models import *


def my_tutors_view(request):
    student = Profile_Student.objects.get(user=request.user)
    if student:
        list_req = Requesting_tutor.objects.filter(student_user_id=student,status='accepted')
    context = {
        'list_req' : list_req,
        'active_tab': 'all_tutors',
    } 
    return render(request,'mytutors/my_tutors.html',context)

def mytutors_ongoing(request):
    student = Profile_Student.objects.get(user=request.user)
    if student:
        list_req = Requesting_tutor.objects.filter(student_user_id=student,status='accepted',is_complete=False)
    context = {
        'list_req' : list_req,
        'active_tab': 'incomplete',
    } 
    return render(request,'mytutors/incomplete_my_tutors.html',context)

def mytutors_complete(request):
    student = Profile_Student.objects.get(user=request.user)
    if student:
        list_req = Requesting_tutor.objects.filter(student_user_id=student,status='accepted',is_complete=True)
    context = {
        'list_req' : list_req,
        'active_tab': 'completed',
    } 
    return render(request,'mytutors/complete_my_tutors.html',context)