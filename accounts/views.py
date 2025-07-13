from django.shortcuts import render,redirect
from django.views import View
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


# Create your views here.
class Register(View):
    def get(self,request):
        return render(request,'registration/register.html')
    
    def post(self,request):
        try:
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password1 = request.POST.get('confirmpassword')
            usertype = request.POST.get('usertype')
            if password == password1:
                    validate_password(password)
                    if password == username:
                        messages.error(request,'password and uname shouldn\'t be same')
                        return redirect('register')
                    if CustomUser.objects.filter(email=email).exists():
                        messages.error(request,'email already exists!')
                        return redirect('register')
                    if CustomUser.objects.filter(username=username).exists():
                        messages.error(request,'username already exists!')
                        return redirect('register')
                    user = CustomUser(
                        first_name = firstname,
                        last_name = lastname,
                        username = username,
                        email = email,
                        usertype = usertype
                    )
                    user.set_password(password)
                    user.full_clean() 
                    user.save()
                    messages.success(request,'Successfully Registered!')
                    return redirect('register')
            else:
                messages.error(request,'password and confirm password didn\'t match!')
                return redirect('register')
            
        except ValidationError as e:
            email_errors = e.message_dict.get('email')
            if email_errors:
                messages.error(request, email_errors[0])
            else:
                messages.error(request, 'Please correct the form fields.')
            return redirect('register')
        
        except Exception as e:
            messages.error(request,f'{str(e)}')
            return redirect('register')
        