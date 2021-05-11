from django import forms
from registerApp.models import UserModel

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model = UserModel
        fields = '__all__'