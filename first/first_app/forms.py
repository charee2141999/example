from django import forms
from first_app.models import info

class newuserform(forms.ModelForm):
    class Meta:
        model = info
        fields = '__all__'
