from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Member

class MemberCreationForm(UserCreationForm):
    class Meta:
        model = Member
        fields = ["email", "first_name", "last_name"]  # Use email instead of username

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({"placeholder": "Enter email"})
        self.fields["first_name"].widget.attrs.update({"placeholder": "Enter first name"})
        self.fields["last_name"].widget.attrs.update({"placeholder": "Enter last name"})
        self.fields["password1"].widget.attrs.update({"placeholder": "Enter password"})
        self.fields["password2"].widget.attrs.update({"placeholder": "Confirm password"})

class MemberChangeForm(UserChangeForm):
    class Meta:
        model = Member
        fields = ["email", "first_name", "last_name"]  # No password fields for updates
