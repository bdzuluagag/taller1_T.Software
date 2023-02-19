from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField()
    last_name = forms.CharField()
    password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Password confirmation ', widget = forms.PasswordInput)
    
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('name', 'last_name', 'email',)
        help_texts = {k:"" for k in fields}
