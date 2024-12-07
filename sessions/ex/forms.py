from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label='username', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}))
    password = forms.CharField(label='password', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}))
    password_confirm = forms.CharField(label='password_confirm', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your password'}))
    
    
class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}))
    password = forms.CharField(label='password', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}))


class TipForm(forms.Form):
    content  = forms.CharField(label='content', max_length=100, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your tip', 'style': 'height: 400px; resize: none;'}))
