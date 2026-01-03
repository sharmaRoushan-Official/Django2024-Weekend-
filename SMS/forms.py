from SMS.models import student
from django import forms 


class studentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name','age','mobileNo','dob','pic']