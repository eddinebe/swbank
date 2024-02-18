from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("edit/", views.edit_profile, name="edit_profile"),
    path("settings/", views.settings, name="settings"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("account_customer/", views.account_customer, name="account_customer"),
    path("account_transfer/", views.make_transfer, name="account_transfer"),
    path("account_create/", views.make_account, name="account_create"),
    path("products/", views.products, name="products"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
