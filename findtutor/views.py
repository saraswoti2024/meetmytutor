from django.shortcuts import render
from profileapp.models import Profile_Tutor
from categories.models import districts,subjects_list
from django.db.models import Q 

def all_tutor_view(request):
    all_subjects = subjects_list.objects.all()
    all_tutors = Profile_Tutor.objects.all() 
    districts_list = districts.objects.all()

    education_level = request.GET.get('education_level')
    subject = request.GET.get('subject')
    district_name = request.GET.get('district')
    tutor_name = request.GET.get('tutorname')

    if education_level:
        all_tutors = all_tutors.filter(education_data__contains=[{'level': education_level}])


    if subject:
        # This is the correct and efficient way to filter for subjects within the JSONField.
        # It checks if any object in 'education_data' list has a 'subjects' array
        # that contains the 'subject' value.
        all_tutors = all_tutors.filter(education_data__contains=[{'subjects': [subject]}])

    # Filter by district
    if district_name:
        # Assumes Profile_Tutor has a direct 'district' field.
        all_tutors = all_tutors.filter(district__iexact=district_name)

    # Filter by tutor_name (first name or last name)
    if tutor_name:
        # Assuming Profile_Tutor has a ForeignKey to User model called 'user'
        # And the User model has 'first_name' and 'last_name'
        all_tutors = all_tutors.filter(
            Q(user__first_name__icontains=tutor_name) |
            Q(user__last_name__icontains=tutor_name)
        )

    context = {
        'tutorlist': all_tutors,
        'district': districts_list, # Pass the list of all districts
        'selected_education_level': education_level, # Pass back selected values for form persistence
        'selected_subject': subject,
        'selected_district': district_name,
        'searched_tutor_name': tutor_name,
        'all_subjects' : all_subjects, # Pass all subjects for the dropdown
    }
    return render(request, 'findtutor/all_tutor.html', context)