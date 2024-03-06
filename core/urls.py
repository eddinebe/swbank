from django.urls import path

from core import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),

    # Client
    path("client_profile/", views.client_edit_profile, name="client_profile"),
    path("client_settings/", views.client_settings, name="client_settings"),
    path("client_dashboard/", views.client_dashboard, name="client_dashboard"),
    path("client_view_accounts/", views.client_view_accounts, name="client_view_accounts"),
    path("client_create_transfer/", views.client_create_transfer, name="client_create_transfer"),
    path("client_create_account/", views.create_account, name="account_create"),

    # Staff
    path("staff_create_account/", views.staff_create_account, name="staff_create_account"),
    path("staff_view_accounts/", views.staff_view_accounts, name="staff_view_accounts"),
    path("staff_view_clients/", views.staff_view_clients, name="staff_view_clients"),

    # Main
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("products/", views.products, name="products"),
    path("about/", views.about_us, name="about_us"),
    path("contact/", views.contact_us, name="contact_us"),

]
