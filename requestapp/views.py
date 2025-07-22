from django.shortcuts import render,get_object_or_404,redirect
from profileapp.models import *
from requestapp.models import Requesting_tutor
from django.contrib import messages
from django.core.exceptions import ValidationError
from categories.models import subjects_list

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Profile_Tutor, Profile_Student, Requesting_tutor, subjects_list

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Profile_Tutor, Profile_Student, Requesting_tutor, subjects_list
from django.contrib.auth.decorators import login_required

@login_required(login_url='log_in')
def tutor_session_request(request, id):
    tutor = get_object_or_404(Profile_Tutor, id=id)
    student = Profile_Student.objects.get(user=request.user)

    # Extract subject names from tutor's education_data JSON
    subject_names = set()
    for level in tutor.education_data:
        subject_names.update(level.get('subjects', []))

    # Get subject objects matching those names
    subjects = subjects_list.objects.filter(subject_name__in=subject_names)

    if request.method == 'POST':
        try:
            selected_subject_ids = request.POST.getlist('subjects')
            selected_subject_ids = [int(sid) for sid in selected_subject_ids if sid.strip().isdigit()]
            mode = request.POST.get('mode')
            time_from = request.POST.get('time_from')
            time_to = request.POST.get('time_to')
            start_date = request.POST.get('date_start')
            end_date = request.POST.get('date_end')
            priceperhour = request.POST.get('perhour')

            data = Requesting_tutor(
                proposed_rate=priceperhour,
                session_start_date=start_date,
                session_end_date=end_date,
                session_time_from=time_from,
                session_time_to=time_to,
                student_user=student,
                tutor_user=tutor,
                mode = mode,
            )
            data.full_clean()  # Validate before saving
            data.save()
            data.subject.set(selected_subject_ids)  # Set ManyToMany subjects

            messages.success(request, 'Request sent successfully!')
            return redirect('tutor_session_request', id)

        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            return redirect('tutor_session_request', id)

    context = {
        'tutor': tutor,
        'subjects': subjects,
    }
    return render(request, 'request_session/request_tutor.html', context)

def request_list(request):
    student = Profile_Student.objects.get(user=request.user)
    list_req = Requesting_tutor.objects.filter(student_user=student)
    context = {
        'list_req' : list_req,
    } 
    return render(request,'request_session/request_view.html',context)