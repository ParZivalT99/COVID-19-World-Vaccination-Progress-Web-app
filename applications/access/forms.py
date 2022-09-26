from django import forms

# from django.contrib import messages
from django.core.validators import validate_slug
from django.contrib.auth import authenticate


from .models import User


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        # max_length=20,
        required=True,
        validators=[validate_slug],
        widget=forms.PasswordInput(attrs={"class": "form-control form-acceso"}),
    )
    isAdmin = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={"class": "form-check-input", "type": "checkbox"}
        ),
    )

    class Meta:
        """Meta definition for Userform"""

        model = User
        fields = ("username", "password")
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control form-acceso"})
        }

    def clean_password(self):

        if len(self.cleaned_data["password"]) <= 7:
            self.add_error(
                "password", "The password must be at least 8 characters long"
            )
        else:
            return self.cleaned_data["password"]


class LoginForm(forms.Form):
    username = forms.CharField(
        # max_length=20,
        required=True,
        validators=[validate_slug],
        widget=forms.TextInput(attrs={"class": "form-control form-acceso"}),
    )
    password = forms.CharField(
        # max_length=20,
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control form-acceso"}),
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        try:
            username = self.cleaned_data["username"]
            password = self.cleaned_data["password"]
            user = User.objects.get(username=self.cleaned_data["username"])

            if not authenticate(username=username, password=password):
                raise forms.ValidationError("User data is not correct")

        except Exception:
            raise forms.ValidationError("This user does not exist")
        return self.cleaned_data
