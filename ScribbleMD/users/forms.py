from django import forms


class RegisterUser(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()


class login_main(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())