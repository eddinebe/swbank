from django.contrib import admin

from core.models import Account, Customer, Rank, Ledger, Staff

admin.site.register(Rank)
admin.site.register(Ledger)
admin.site.register(Customer)
admin.site.register(Account)
admin.site.register(Staff)
# Register your models here.
