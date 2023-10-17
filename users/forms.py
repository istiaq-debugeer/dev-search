import attrs
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Skill
from django.contrib.auth.models import  User

class UserCreateForm(UserCreationForm):
    class Meta:
        model=User
        fields=('first_name','last_name','username','email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields='__all__'
        exclude=['user']

    def __int__(self,*args,**kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget,attrs.update({'class':'input'})

class SkillForm(forms.ModelForm):
    class Meta:
        model=Skill
        fields='__all__'
        exclude=['owner']

    def __int__(self,*args,**kwargs):
        super(SkillForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget,attrs.update({'class':'input'})
