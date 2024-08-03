from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User


class UserAdminCreationForm(forms.ModelForm):
    """
    form for creating new users in admin panel.
    """

    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "phone",
            "first_name",
            "last_name",
        ]

    def clean_password_confirm(self):
        data = self.cleaned_data
        if (
            data["password"]
            and data["password_confirm"]
            and data["password"] != data["password_confirm"]
        ):
            raise forms.ValidationError("Passwords don't match")
        return data["password_confirm"]

    def save(self, commit: True):
        user = super().save(commit=False)
        user.set_password(self.data["password"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """
    form for updating users in admin panel.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = "__all__"


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control "

    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
