from django.urls import include, path
from rest_framework import routers

from core import views

app_name = "core"

router = routers.DefaultRouter()
router.register(r"accounts", views.AccountViewSet)
router.register(r"clients", views.CustomerViewSet)
router.register(r"ledger", views.LedgerViewSet)
router.register(r"transfer", views.TransferViewSet, basename="transfer")

urlpatterns = [
    # API
    path("api/", include(router.urls)),
    # Main
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("main_products/", views.main_products, name="main_products"),
    path("main_about_us/", views.main_about_us, name="main_about_us"),
    path("main_contact_us/", views.main_contact_us, name="main_contact_us"),
    path("main_news/", views.main_news, name="main_news"),
    path("main_stocks/", views.main_stocks, name="main_stocks"),
    # Staff
    path("staff_dashboard/", views.staff_dashboard, name="staff_dashboard"),
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
