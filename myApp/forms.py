from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Students

class SignupForms(UserCreationForm):
    username = forms.CharField(label='username',widget=forms.TextInput(attrs={"class":"form-control",'placeholder':" write a username "}))
    password1=forms.CharField(label="password",widget=forms.PasswordInput(attrs={"class":'form-control','placeholder':'type you password'}))
    password2=forms.CharField(label="confirm-password",widget=forms.PasswordInput(attrs={"class":'form-control','placeholder':'re-type you password'}))
    
    class Meta:
        model=User
        fields=["username",'first_name','last_name','email']
        labels={"first_name":"First Name",'last-name':"Last Name",'email':"Email"}
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'write your first name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'write your last name'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'write your email'}),
        }

class LoginForms(AuthenticationForm):
    username=forms.CharField(label="username",widget=forms.TextInput(attrs={"class":"form-control",'placeholder':" write a username "}))
    password=forms.CharField(label="password",widget=forms.PasswordInput(attrs={"class":"form-control",'placeholder':" type your password "}))

class StudentsForms(forms.ModelForm):
    class Meta:
        model=Students
        fields=['name','roll','address','email','img']
        labels={'name':"Name",'roll':'Roll','address':'Address','img':"Img"}
        widgets={
            "name":forms.TextInput(attrs={"class":'form-control',"placeholder":"enter students name"}),
            "roll":forms.TextInput(attrs={"class":'form-control',"placeholder":"enter students roll"}),
            "address":forms.Textarea(attrs={"class":'form-control',"placeholder":"enter students address"}),
            "email":forms.TextInput(attrs={"class":'form-control',"placeholder":"enter students email"}),
            "img":forms.FileInput(attrs={"class":'form-control'}),
        }
      