from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Profile_Tutor(models.Model):
    user = models.OneToOneField(CustomUser,related_name='profile',on_delete=models.CASCADE)
    age = models.IntegerField(null=False,blank=False)
    gender = models.CharField(max_length=50,null=False,blank=False)
    qualification = models.CharField(max_length=100,null=False,blank=False)
    session_price = models.IntegerField(null=False,blank=False)
    cv = models.FileField(upload_to="cv_tutor",null=False,blank=False)
    district = models.CharField(max_length=100,null=False,blank=False)
    address = models.CharField(max_length=100,null=False,blank=False)
    longitude = models.DecimalField(max_digits=20,decimal_places=10,null=True,blank=True)
    latitude = models.DecimalField(max_digits=20,decimal_places=10,null=True,blank=True)
    desc = models.TextField(null=True,blank=True,default="no description")
    profile_img = models.ImageField(upload_to="profile_image_tutor",null=True,blank=True)
    education_data = models.JSONField(help_text="List of education levels and subjects.",null=False,blank=False)
    