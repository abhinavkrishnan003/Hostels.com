from dataclasses import fields
from socket import fromshare
from django import forms
from dothack2022_app.models import studform

class Newstudform(forms.ModelForm):
    class Meta():
        model = studform
        fields = '__all__'
