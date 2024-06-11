from django import forms

class SignupForm(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    password1=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control"}))

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control"}))