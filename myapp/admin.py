from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import StudentModel
# Register your models here.

@register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','id','age','photo']