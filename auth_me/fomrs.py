from django import forms
from account.models import Account


class LoginForm(forms.Form):
    login = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))


class SignupForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "id": "inlineFormInputGroup",
                                                             "placeholder": "John Doe"}))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control", "id": "inputEmail3", "placeholder": "exemple@email.com"}))

    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={"class": "form-control", 'label': 'confirm pasword', "placeholder": " your secret password"}))

    password2 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": " Confirm your password"}))

    Are_you_an_external_agent = forms.BooleanField(required=False,
                                                   widget=forms.CheckboxInput(
                                                       attrs={"class": "form-check", "id": "gridCheck1"}))

    class Meta:
        model = Account
        fields = ("username", "email", "password", "password2", "is_external")

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password_val = self.cleaned_data.get('password2')
        if password != password_val:
            raise forms.ValidationError(" password mismatch")
        return data

    def clean_username(self):
        agent = self.cleaned_data.get('username')
        qs = Account.objects.filter(username=agent)
        if qs:
            raise forms.ValidationError("user is already in data base")
        return agent

    def clean_email(self):
        mail = self.cleaned_data.get('email')
        qs = Account.objects.filter(email=mail)
        if '@jumia.com' not in mail:
            raise forms.ValidationError(" we don't accepte login with personal emails, please try with jumia email")
        if qs:
            raise forms.ValidationError("Email already in use")
        return mail
