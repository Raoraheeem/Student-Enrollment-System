from django.core import validators
from django import forms
from.models import User

class Marks(forms.ModelForm):
    class Meta:
     model=User
     fields=['Total_marks','Obtained_marks']
    