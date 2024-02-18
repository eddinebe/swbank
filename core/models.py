from django.contrib.auth.models import User
from django.db import models


class Rank(models.Model):
    name = models.CharField(max_length=35, unique=True, db_index=True)
    value = models.IntegerField(unique=True, db_index=True)

    def __str__(self):
        return f"{self.value}:{self.name}"


class Position(models.Model):
    name = models.CharField(max_length=35, unique=True, db_index=True)
    value = models.IntegerField(unique=True, db_index=True)

    def __str__(self):
        return f"{self.value}:{self.name}"


class Customer(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.PROTECT)
    rank = models.ForeignKey(Rank, default=2, on_delete=models.PROTECT)
    phone = models.CharField(max_length=35, db_index=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.rank}"


class Staff(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.PROTECT)
    position = models.ForeignKey(Position, default=2, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.position}"


class KYC(models.Model):
    poi_image = models.ImageField(upload_to="kyc/poi/", blank=False, null=False)
    poa_image = models.ImageField(upload_to="kyc/poa/", blank=False, null=False)


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, db_index=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class Ledger(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LoanForm


@login_required
def loan_application(request):
    customer = (
        request.user.customer
    )  # Assuming all users have a corresponding Customer profile

    # Check if the user's rank is silver or gold
    if customer.rank.name in ["silver", "gold"]:
        if request.method == "POST":
            form = LoanForm(request.POST)
            if form.is_valid():
                # Process the form data
                # Assuming you save the form data and redirect the user to a success page
                return redirect("loan_success")
        else:
            form = LoanForm()
        return render(request, "loan_application.html", {"form": form})
    else:
        return redirect("test")  # Redirecting to test.html
