from django import forms
from .models import Voter

class VoterForm(forms.ModelForm):
    class Meta:
        model = Voter
        fields = ['name', 'voter_id', 'dob']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }
