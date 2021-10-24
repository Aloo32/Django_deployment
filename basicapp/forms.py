from .models import UserProfileInfo
from django import forms
from django.contrib.auth.models import User

class Userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}))

    class Meta():
        model = User
        fields = ('username','email','password')
        widgets = {
            'username':forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}),
            'email':forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}),
         

        }


class UserProfileInfoForm(forms.ModelForm): 
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
        widgets = {
            'portfolio_site':forms.URLInput(attrs={'class': 'form-control','placeholder':'Website'}),

         

        }




