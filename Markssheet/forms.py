from django.core import validators
from django import forms
from .models import Markssheet

class Uploadmarks(forms.ModelForm):
     class Meta:
       model=Markssheet
       fields=['Maths','Physics','Biology','Chemistry','English','Total','Percentage']
       widgets={
           'Maths': forms.NumberInput(attrs={'class':'form-control'}),
           'Physics': forms.NumberInput(attrs={'class':'form-control'}),
           'Chemistry': forms.NumberInput(attrs={'class':'form-control'}),
           'Biology': forms.NumberInput(attrs={'class':'form-control'}),
           'English': forms.NumberInput(attrs={'class':'form-control'}),
           'Total': forms.NumberInput(attrs={'class':'form-control'}),
           'Percentage': forms.NumberInput(attrs={'class':'form-control'})
       }