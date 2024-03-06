from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.db import transaction
from django.shortcuts import redirect, render
from django.contrib.auth import login
from core.forms import CustomerRegistrationForm

from .forms import AccountForm, ContactForm, EditProfileForm, KYCForm, TransferForm
from .models import Account, Customer, Ledger


# Main

def index(request):
    return render(request, "core/main/index.html")


def products(request):
    return render(request, "core/main/main_products.html")


def about_us(request):
    return render(request, "core/main/main_about_us.html")


def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            EmailMessage(
                "Contact Form Submission from {}".format(name),
                message,
                "form-response@example.com",  # Send from (your website)
                ["admin@admin.com"],  # Send to (your admin email)
                [],
                reply_to=[email],  # Email from the form to get back to
            ).send()

            return redirect("core/main/main_contact_us.html")
    else:
        form = ContactForm()
    return render(request, "core/main/main_contact_us.html", {"form": form})


def register(request):

    if request.method == "POST":
        user_form = CustomerRegistrationForm(request.POST)
        kyc_form = KYCForm(request.POST, request.FILES)

        if user_form.is_valid() and kyc_form.is_valid():
            user = user_form.save()
            phone_number = request.POST["phone_number"]

            customer = Customer.objects.create(user=user, phone=phone_number)
            account = Account.objects.create(user=user, name="main")

            # Save KYCForm with the associated Customer
            kyc_form.instance.customer = customer

            # Access the images directly from the form's instance
            kyc_form.instance.poi_image = kyc_form.cleaned_data["poi_image"]
            kyc_form.instance.poa_image = kyc_form.cleaned_data["poa_image"]
            kyc_form.save()

            login(request, user)

            return redirect("registration:register.html")

    else:
        user_form = CustomerRegistrationForm()
        kyc_form = KYCForm()

    return render(
        request,
        "registration/register.html",
        {"user_form": user_form, "kyc_form": kyc_form},
    )


@login_required
def dashboard(request):
    user = request.user

    # Retrieve the latest transfers associated with the user's accounts
    latest_transfers = Ledger.objects.filter(account__user=user).order_by("-date")[:10]

    context = {
        "user": user,
        "latest_transfers": latest_transfers,
    }

    return render(request, "core/dashboard.html", context)


@login_required
@transaction.atomic
def create_transfer(request):
    if request.method == "POST":
        form = TransferForm(request.POST)
        if form.is_valid():
            source_account = form.cleaned_data["source_account"]
            destination_account = form.cleaned_data["destination_account"]
            amount = form.cleaned_data["amount"]
            description = form.cleaned_data["description"]

            # Deduct amount from source account
            source_account.balance -= amount
            source_account.save()

            # Add amount to destination account
            destination_account.balance += amount
            destination_account.save()

            # Create ledger entries
            Ledger.objects.create(
                account=source_account, amount=-amount, description=description
            )
            Ledger.objects.create(
                account=destination_account, amount=amount, description=description
            )

            # Redirect to dashboard or success page
            return redirect("core:dashboard")
    else:
        form = TransferForm()
    return render(request, "core/account_transfer.html", {"form": form})


@login_required
def create_account(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            # Get the current user
            user = request.user
            name = form.cleaned_data["name"]
            # Create a new instance of the Account model with form data and user
            new_account = Account(name=name, user=user)
            # Save the new account to the database
            new_account.save()
            # Optionally, redirect the user to a success page or perform other actions
            return redirect("core:account_create")
    else:
        form = AccountForm()
    return render(request, "core/account_create.html", {"form": form})


@login_required
def account_customer(request):
    # Retrieve accounts associated with the logged-in user
    user = request.user
    accounts = Account.objects.filter(user=user)
    context = {"accounts": accounts}
    return render(request, "core/account_customer.html", context)


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("core:edit_profile")
    else:
        form = EditProfileForm(instance=request.user)

    return render(
        request, "core/edit_profile.html", {"user": request.user, "form": form}
    )


@login_required
def settings(request):
    return render(request, "core/settings.html")


# STAFF:


@login_required
def account_staff(request):
    accounts = Account.objects.all()
    context = {"accounts": accounts}
    return render(request, "core/account_staff.html", context)


@login_required
def customer_staff(request):
    # Retrieve all accounts in the system
    customers = Customer.objects.all()
    context = {"customers": customers}
    return render(request, "core/customer_staff.html", context)
