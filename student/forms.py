from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
	class Meta:
		model=Student
		fields="__all__"

class ProfileForm(forms.Form):
   name = forms.CharField(max_length = 100)
   picture = forms.ImageField()