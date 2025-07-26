from django.shortcuts import render,redirect,get_object_or_404
from profileapp.models import Profile_Tutor
from categories.models import districts,subjects_list
from django.db.models import Q 
from django.contrib.auth.decorators import login_required
from requestapp.models import Requesting_tutor
from django.contrib import messages
from geopy.distance import geodesic
from mytutorapp.models import Feedback
from django.db.models import Avg


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
def nearest_tutors_list_view(request):
    try:
        user_lat = request.GET.get("lat")
        user_lng = request.GET.get("lng")

        if not user_lat or not user_lng:
            messages.error(request, "Latitude and Longitude are required.")
            return redirect('home')

        user_location = (float(user_lat), float(user_lng))
        tutors = Profile_Tutor.objects.filter(latitude__isnull=False, longitude__isnull=False)

        tutor_list = []
        for tutor in tutors:
            try:
                tutor_location = (float(tutor.latitude), float(tutor.longitude))
                distance = geodesic(user_location, tutor_location).km

                # Only add if within 5km
                if distance <= 5.0:
                    tutor_list.append({
                        "id": tutor.id,
                        "first_name": tutor.user.first_name,
                        "last_name": tutor.user.last_name,
                        "qualification": tutor.qualification,
                        "session_price": tutor.session_price,
                        "district": tutor.district,
                        "education_data": tutor.education_data,
                        "profile_img": tutor.profile_img,
                        "latitude": float(tutor.latitude),
                        "longitude": float(tutor.longitude),
                        "distance": round(distance, 3),
                    })
            except Exception:
                continue  # Skip tutor with invalid lat/lng

        sorted_nearby = sorted(tutor_list, key=lambda x: x["distance"])

        return render(request, 'findtutor/nearby_tutor.html', {
            'nearest': sorted_nearby,
            'user_lat': user_lat,
            'user_lng': user_lng
        })

    except Exception as e:
        messages.error(request, f'Error: {str(e)}')
        return redirect('home')
    
@login_required(login_url='log_in')
def view_tutor_profile_view(request,id):
    profile_id = get_object_or_404(Profile_Tutor,id=id)
    feedbacks = Feedback.objects.filter(tutor_user=profile_id).order_by('-created_at')
    avg_rating = feedbacks.aggregate(Avg('rating'))['rating__avg'] or 0
    avg_rating = round(avg_rating, 1)
    
    # Calculate average rating (optional)
    avg_rating = feedbacks.aggregate(Avg('rating'))['rating__avg'] or 0
    avg_rating = round(avg_rating, 1)
    context = {
        'profile_id' : profile_id,
        'feedbacks': feedbacks,
        'avg_rating': avg_rating,
    }
    return render(request,'profile_detail/tutor_view_profile.html',context)

@login_required(login_url='log_in')
def view_tutor_profile_view2(request,id):
    profile_id2 = get_object_or_404(Requesting_tutor,id=id)
    feedbacks = Feedback.objects.filter(tutor_user=profile_id2.tutor_user).order_by('-created_at')
    avg_rating = feedbacks.aggregate(Avg('rating'))['rating__avg'] or 0
    avg_rating = round(avg_rating, 1)
    profile2 = profile_id2.tutor_user
    context = {
        'profile_id2' : profile2,
        'feedbacks': feedbacks,
        'avg_rating': avg_rating,
    }
    return render(request,'profile_detail/tutor_view_profile2.html',context)

@login_required(login_url='log_in')
def view_student_profile(request,id):
    student_id2 = get_object_or_404(Requesting_tutor,id=id)
    student_id = student_id2.student_user
    context = {
        'student_id' : student_id
    }
    return render(request,'profile_detail/student_view_profile.html',context)

@login_required(login_url='log_in')
def detect_location_view(request):
    return render(request, 'findtutor/detect_location.html')
