from django import forms
from django.contrib.auth.models import User
from basicapp.models import UserProfileInfo


def check_for_z(value):
    if value[0].lower()!='z':
        raise forms.ValidationError("Name doesnt start with z")

class FormName(forms.Form):
    name=forms.CharField(validators=[check_for_z])
    email=forms.EmailField()
    verifymail=forms.EmailField(label="Enter your mail again")
    text=forms.CharField(widget=forms.Textarea)
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,)

def clean(self):
    all_clean_data=super().clean()
    email=all_clean_data['email']
    vmail=all_clean_data['verifymail']
    if email!=vmail:
        raise forms.ValidationError("EMail should match")

     #catch bot

    def clean_botcatcher(self):
        botcatcher=self.cleaned_data['botcatcher']         #bakchodi
        if len(botcatcher)>0:
            raise forms.ValidationError("Gotcha Bott")
        return botcatcher

class UserForm(forms.ModelForm):
    #password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password')

class UserProfileInfo(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('portfolio_site','profile_pic')
