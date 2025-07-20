from django.shortcuts import render
from profileapp.models import Profile_Tutor
from categories.models import districts,subjects_list
from django.db.models import Q 
from django.contrib.auth.decorators import login_required


def all_tutor_view(request):
    all_subjects = subjects_list.objects.all()
    all_tutors = Profile_Tutor.objects.all().order_by('id') 
    districts_list = districts.objects.all()

    education_level = request.GET.get('education_level')
    subject = request.GET.get('subject')
    district_name = request.GET.get('district')
    tutor_name = request.GET.get('tutorname')

    if education_level:
        all_tutors = all_tutors.filter(education_data__contains=[{'level': education_level}])

    if subject:
        all_tutors = all_tutors.filter(education_data__contains=[{'subjects': [subject]}])

    if district_name:
        all_tutors = all_tutors.filter(district__iexact=district_name)

    if tutor_name:
        all_tutors = all_tutors.filter(
            Q(user__first_name__icontains=tutor_name) |
            Q(user__last_name__icontains=tutor_name)
        )

    context = {
        'tutorlist': all_tutors,
        'district': districts_list, 
        'selected_education_level': education_level,
        'selected_subject': subject,
        'selected_district': district_name,
        'searched_tutor_name': tutor_name,
        'all_subjects' : all_subjects, 
    }
    return render(request, 'findtutor/all_tutor.html', context)

@login_required(login_url='log_in')
def nearby_tutor_view(request):
    return render(request,'findtutor/nearby_tutor.html')

@login_required(login_url='log_in')
def view_tutor_profile_view(request,id):
    profile_id = Profile_Tutor.objects.get(id=id)
    context = {
        'profile_id' : profile_id
    }
    return render(request,'profile_detail/tutor_view_profile.html',context)
