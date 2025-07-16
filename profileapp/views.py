from django.shortcuts import render,redirect
from django.views import View
from categories.models import districts
from .models import Profile_Tutor
from django.contrib import messages
from django.core.exceptions import ValidationError
import json
# Create your views here.


class tutor_profile_view(View):
    def get(self,request):
        return render(request,'profile/tutor_profile1.html')
    
def edit_tutor_profile(request):
        if not request.user.is_authenticated:
            return redirect('log_in')
        district = districts.objects.all()
        try:
            data = Profile_Tutor.objects.get(user=request.user)
        except Profile_Tutor.DoesNotExist:
            data = None
        if request.method == 'POST' or request.FILES :
            try:
                if data is None:
                    data = Profile_Tutor(user=request.user)
                data.age = request.POST.get('age')
                data.profile_img = request.FILES.get('profile_img')
                data.qualification = request.POST.get('qualification')
                data.session_price = request.POST.get('session_price')
                data.district = request.POST.get('district')
                data.address = request.POST.get('address')
                data.gender = request.POST.get('gender')
                if data.longitude:
                     data.longitude = request.POST.get('longitude')
                if data.latitude:
                     data.latitude = request.POST.get('latitude')
                data.cv = request.FILES.get('cv')or data.cv
                if not data.cv:
                    messages.error(request, 'CV is required.')
                    return redirect('edit_tutor_profile')
                data.desc = request.POST.get('description')
                education_levels = []
                i = 0
                while True:
                    level_key = f"educationLevels[{i}][level]"
                    subject_key = f"educationLevels[{i}][subjects][]"

                    level = request.POST.get(level_key)
                    subjects = request.POST.getlist(subject_key)

                    if not level:
                        break

                    education_levels.append({
                        "level": level,
                        "subjects": subjects
                    })
                    i += 1

                data.education_data = education_levels
                data.full_clean()
                data.save()
                messages.success(request,'updated successfully!')
                return redirect('tutor_profile')
            except ValidationError as ve:
                error_count = 0
                for field, errors in ve.message_dict.items():
                    for error in errors:
                        messages.error(request, f"{field.capitalize()}: {error}")
                        error_count += 1
                        if error_count == 3:
                            break
                    if error_count == 3:
                        break

            except Exception as e:
                messages.error(request, str(e))
                return redirect('edit_tutor_profile')
          # Prepare preloaded education data as JSON to pass to template
        education_data_json = json.dumps(data.education_data) if data and data.education_data else '[]'
        context = {
            'district' : district,
            'education_data_json': education_data_json,
        } 
        
        return render(request,'profile/edit_tutor_profile.html',context)
    