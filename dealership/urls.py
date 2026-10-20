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
    post_review_page,
)
from accounts.dealers import (
    get_all_dealers,
    fetch_dealers,
    get_dealer_by_id,
    get_dealers_by_state,
    dealer_detail_page,
)
from accounts.car_api import get_all_car_makes

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", login_user, name="login_user"),
    path("djangoapp/login", djangoapp_login, name="djangoapp_login"),
    path("logout/", logout_user, name="logout_user"),
    path("djangoapp/logout", djangoapp_logout, name="djangoapp_logout"),

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
    path(
        "dealer/<int:dealer_id>/submit-review/",
        post_review_page,
        name="post_review_page",
    ),

    path("dealers/", get_all_dealers, name="get_all_dealers"),
    path("fetchDealers", fetch_dealers, name="fetch_dealers"),
    path(
        "dealers/by-state/",
        get_dealers_by_state,
        name="get_dealers_by_state",
    ),
    path(
        "dealer-detail/<int:dealer_id>/",
        dealer_detail_page,
        name="dealer_detail_page",
    ),
    path(
        "dealer/<int:dealer_id>/",
        get_dealer_by_id,
        name="get_dealer_by_id",
    ),
    path(
        "fetchDealer/<int:dealer_id>",
        get_dealer_by_id,
        name="fetch_dealer_by_id",
    ),
    path(
        "fetchDealers/<str:state>",
        get_dealers_by_state,
        name="fetch_dealers_by_state",
    ),
    path("car-makes/", get_all_car_makes, name="get_all_car_makes"),
]
