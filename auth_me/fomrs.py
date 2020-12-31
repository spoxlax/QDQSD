from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "id": "inlineFormInputGroup",
                                                             "placeholder": "John Doe"}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control", "id": "inputEmail3", "placeholder": "exemple@email.com"}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "id": "exampleInputPassword1", "placeholder": " your secret password"}))
    password_validation = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "id": "exampleInputPassword1", "placeholder": " Confirm your password"}))
    Are_you_an_external_agent = forms.BooleanField(required=False,
                                                   widget=forms.CheckboxInput(
                                                       attrs={"class": "form-check", "id": "gridCheck1",
                                                              "label": " yes i am"}))

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password_val = self.cleaned_data.get('password_validation')
        if password!= password_val:
            raise forms.ValidationError(" password mismatch")
        return password

    # def clean_username(self):
    #     agent = self.cleaned_data.get('username')
    #     qs = User.objects.filter(username=agent)
    #     print(qs)
    #     if qs:
    #         raise forms.ValidationError("user is already in data base")
    #     return agent
