from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import EmailValidator

from core.models import KYC, Account, Position


class KYCForm(forms.ModelForm):
    class Meta:
        model = KYC
        fields = ["poi_image", "poa_image"]


class ClientRegistrationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=20, required=True)
    kyc_form = KYCForm()

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]


class StaffRegistrationForm(UserCreationForm):
    position = forms.ModelChoiceField(queryset=Position.objects.all(), initial=2)

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]


class ContactForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField(validators=[EmailValidator()])
    phone = forms.CharField(max_length=20, required=False)
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["name"]


class LoanForm(forms.ModelForm):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    loan_type = forms.ChoiceField(
        choices=[("personal", "Personal Loan"), ("business", "Business Loan")]
    )

    class Meta:
        model = Account
        fields = []  # Since you want to include additional fields, leave this empty


class TransferForm(forms.Form):
    source_account = forms.ModelChoiceField(
        queryset=Account.objects.all(), label="Source Account"
    )
    destination_account = forms.ModelChoiceField(
        queryset=Account.objects.all(), label="Destination Account"
    )
    amount = forms.DecimalField(label="Amount")
    description = forms.CharField(label="Description", max_length=255)


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]
