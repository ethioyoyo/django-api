from django import forms
from hostgenapp.models import hosts, MyUserProfile, networks
from django.contrib.auth.models import User

class api_host_gen(forms.ModelForm):
   class Meta:
      model = hosts
      fields = '__all__'

class api_net_gen(forms.ModelForm):
    class Meta():
        model = networks
        fields = '__all__'


class MyUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class MyUserProfileForm(forms.ModelForm):
    class Meta():
        model = MyUserProfile
        fields = ('dep_name','profile_pic')


class generate_hosts_form(forms.Form):
    no_hosts = forms.CharField()

