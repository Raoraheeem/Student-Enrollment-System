from django.contrib import admin
from .models import Markssheet


@admin.register(Markssheet)
class MarkssheetAdmin(admin.ModelAdmin):
    list_display=['Maths','Physics','Biology','Chemistry','English','Total','Percentage']

# Register your models here.
