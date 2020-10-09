from django import forms
from .models import *


class AddForm(forms.Form):
        user_name = forms.CharField(label="Username", widget=forms.TextInput(), required = True)
        password = forms.CharField(label="Password", widget=forms.PasswordInput(), required = True)
        first_name = forms.CharField(label="First Name", widget=forms.TextInput(), required = True)
        last_name = forms.CharField(label="Last Name", widget=forms.TextInput(), required = True)
        email = forms.CharField(label="Email Address", widget=forms.TextInput(), required = True)
        age = forms.CharField(label="Age", widget=forms.TextInput(), required = True)
        sport = forms.ModelMultipleChoiceField(label='Sports',widget = forms.CheckboxSelectMultiple, queryset=Activities.objects.all())
