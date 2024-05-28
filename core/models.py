from django.contrib.auth.models import User
from django.db import models


class Rank(models.Model):
    name = models.CharField(max_length=35, unique=True, db_index=True)
    value = models.IntegerField(unique=True, db_index=True)

    def __str__(self):
        return f"{self.name}"


class Position(models.Model):
    name = models.CharField(max_length=35, unique=True, db_index=True)
    value = models.IntegerField(unique=True, db_index=True)

    def __str__(self):
        return f"{self.name}"


class Customer(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.PROTECT)
    rank = models.ForeignKey(Rank, default=1, on_delete=models.PROTECT)
    phone = models.CharField(max_length=35, db_index=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Staff(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.PROTECT)
    position = models.ForeignKey(Position, default=1, on_delete=models.PROTECT)
    phone = models.CharField(max_length=35, db_index=True)
    is_staff = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.position.name}"


class KYC(models.Model):
    poi_image = models.ImageField(upload_to="kyc/poi/", blank=False, null=False)
    poa_image = models.ImageField(upload_to="kyc/poa/", blank=False, null=False)


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, db_index=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name


# class CreditCard(model.Model):
#    account = models.ForeignKey(Account, on_delete=models.PROTECT)
#    number =
#    expiration_date =
#    CVV =


class Ledger(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Account: {self.account}, Amount: {self.amount}, Description: {self.description}, Date: {self.date}"
