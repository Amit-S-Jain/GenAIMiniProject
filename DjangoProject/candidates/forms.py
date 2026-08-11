# candidates/forms.py
from django import forms
from .models import Candidates

class ResumeUploadForm(forms.Form):
    resume = forms.FileField()

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidates
        fields = "__all__"
