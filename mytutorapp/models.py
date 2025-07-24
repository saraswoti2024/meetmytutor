from django.db import models
from accounts.models import CustomUser
from profileapp.models import *
# Create your models here.
# class Feedback(models.Model):
#     tutor_user = models.ForeignKey(Profile_Tutor,on_delete=models.CASCADE)
#     student_user = models.ForeignKey(Profile_Tutor,on_delete=models.CASCADE)
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     rating = models.IntegerField()
#     comment = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username} - {self.rating} Stars"