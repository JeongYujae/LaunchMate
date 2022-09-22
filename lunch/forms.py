from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields=['title','author','date']
        #좀 알아보기
        # widgets={
        #     'caption': forms.Textarea
        # }
