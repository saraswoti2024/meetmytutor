from django.contrib import admin
from .models import districts
# Register your models here.

@admin.register(districts)
class District(admin.ModelAdmin):
    list_display = ['id','name']