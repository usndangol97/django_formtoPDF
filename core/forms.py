from django import forms
from .models import UserInfo

class Form(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields ='__all__'
