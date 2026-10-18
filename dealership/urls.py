from django.contrib import admin
from django.urls import path
from accounts.views import login_user, logout_user
from accounts.reviews import get_dealer_reviews
from accounts.dealers import get_all_dealers, get_dealer_by_id, get_dealers_by_state

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", login_user, name="login_user"),
    path("logout/", logout_user, name="logout_user"),
    path(
        "dealer/<int:dealer_id>/reviews/",
        get_dealer_reviews,
        name="get_dealer_reviews",
    ),
    path("dealers/", get_all_dealers, name="get_all_dealers"),
    path("dealers/by-state/", get_dealers_by_state, name="get_dealers_by_state"),
    path("dealer/<int:dealer_id>/", get_dealer_by_id, name="get_dealer_by_id"),
]
