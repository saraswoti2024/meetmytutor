from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home/index.html')

def tutor_home(request):
    return render(request,'home/index_tutor.html')