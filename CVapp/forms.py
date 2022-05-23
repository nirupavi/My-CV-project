from django import forms
from .models import Resume
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class signupform (UserCreationForm):
    password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email']
        labels = {'email': 'Email'}

class loginform(forms.Form):
    name = forms.CharField(max_length=70)
    email = forms.EmailField(max_length=70)
    password = forms.CharField(widget=forms.PasswordInput)

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'
        labels = {'name': 'Full Name','email':'Email ID','pin':'PIN Code','mobile':'Mobile No.','profile_image':'Profile Image',
                  'file':'Document'}
        widgets = {
             'name':forms.TextInput(attrs={'class':'form-control'}),
             'email': forms.EmailInput(attrs={'class': 'form-control'}),
             'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
             'locality': forms.TextInput(attrs={'class': 'form-control'}),
             'city': forms.TextInput(attrs={'class': 'form-control'}),
             'pin': forms.NumberInput(attrs={'class': 'form-control'}),
             'state': forms.TextInput(attrs={'class': 'form-control'}),
             'School': forms.TextInput(attrs={'class': 'form-control'}),
             'School_marks': forms.NumberInput(attrs={'class': 'form-control'}),
             'Degree': forms.TextInput(attrs={'class': 'form-control'}),
             'University': forms.TextInput(attrs={'class': 'form-control'}),
             'Degree_percentage': forms.NumberInput(attrs={'class': 'form-control'}),
             'previous_roll': forms.TextInput(attrs={'class': 'form-control'}),
             'previous_experience': forms.TextInput(attrs={'class': 'form-control'}),
             'Tech_skill': forms.Textarea(attrs={'class': 'form-control'}),
             'job_city': forms.TextInput(attrs={'class': 'form-control'}),
        }