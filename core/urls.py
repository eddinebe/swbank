from django.urls import path

from core import views

app_name = "core"

urlpatterns = [
    # Main
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("main_products/", views.main_products, name="main_products"),
    path("main_about_us/", views.main_about_us, name="main_about_us"),
    path("main_contact_us/", views.main_contact_us, name="main_contact_us"),
    # Staff
    path(
        "staff_create_account/",
        views.client_create_account,
        name="staff_create_account",
    ),
    path("staff_view_accounts/", views.staff_view_accounts, name="staff_view_accounts"),
    path("staff_view_clients/", views.staff_view_clients, name="staff_view_clients"),
    # Client
    path("client_profile/", views.client_profile, name="client_profile"),
    path("client_settings/", views.client_settings, name="client_settings"),
    path("client_dashboard/", views.client_dashboard, name="client_dashboard"),
    path(
        "client_view_accounts/", views.client_view_accounts, name="client_view_accounts"
    ),
    path(
        "client_create_transfer/",
        views.client_create_transfer,
        name="client_create_transfer",
    ),
    path(
        "client_create_account/",
        views.client_create_account,
        name="client_create_account",
    ),
]
