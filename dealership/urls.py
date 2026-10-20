
from django.contrib import admin
from django.urls import path

from accounts.views import (
    login_user,
    logout_user,
    djangoapp_login,
    djangoapp_logout,
)
from accounts.reviews import (
    get_dealer_reviews,
    fetch_dealer_reviews,
)
from accounts.dealers import (
    get_all_dealers,
    get_dealer_by_id,
    get_dealers_by_state,
)
from accounts.car_api import get_all_car_makes

urlpatterns = [
    path("admin/", admin.site.urls),

    # Login endpoints
    path("login/", login_user, name="login_user"),
    path("djangoapp/login", djangoapp_login, name="djangoapp_login"),

    # Logout endpoints
    path("logout/", logout_user, name="logout_user"),
    path("djangoapp/logout", djangoapp_logout, name="djangoapp_logout"),

    # Dealer reviews
    path(
        "dealer/<int:dealer_id>/reviews/",
        get_dealer_reviews,
        name="get_dealer_reviews",
    ),
    path(
        "fetchReviews/dealer/<int:dealer_id>",
        fetch_dealer_reviews,
        name="fetch_dealer_reviews",
    ),

    # Dealer endpoints
    path("dealers/", get_all_dealers, name="get_all_dealers"),
    path(
        "dealers/by-state/",
        get_dealers_by_state,
        name="get_dealers_by_state",
    ),
    path(
        "dealer/<int:dealer_id>/",
        get_dealer_by_id,
        name="get_dealer_by_id",
    ),

    # Car makes
    path("car-makes/", get_all_car_makes, name="get_all_car_makes"),
]
