from django import forms
from Footballers.models import Footballers

class FootballerForm(forms.ModelForm):
    class Meta:
        model = Footballers
        fields = "__all__"

