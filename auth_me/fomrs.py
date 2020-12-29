from django import forms


class SignupForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "id": "inlineFormInputGroup"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "id": "inputEmail3"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "id": "exampleInputPassword1"}))
    password_validation = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "id": "exampleInputPassword1"}))
    ext_check = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"class": "form-check", "id": "gridCheck1", "label": " yes i am"}))
