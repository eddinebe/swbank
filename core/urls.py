from django.urls import path

from core import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("settings/", views.settings, name="settings"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("account_customer/", views.account_customer, name="account_customer"),
    path("account_transfer/", views.create_transfer, name="account_transfer"),
    path("account_create/", views.create_account, name="account_create"),½
    path("products/", views.products, name="products"),
    path("about/", views.about_us, name="about_us"),
    path("contact/", views.contact_us, name="contact_us"),
]
