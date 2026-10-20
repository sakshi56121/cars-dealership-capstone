from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_GET
from django.http import JsonResponse


def analyze_sentiment(review_text):
    """Classify review text using simple keyword matching."""
    text = review_text.lower()

    positive_words = {
        "great", "excellent", "good", "helpful", "friendly",
        "smooth", "easy", "love", "happy", "wonderful",
    }
    negative_words = {
        "bad", "poor", "terrible", "awful", "worst",
        "rude", "slow", "disappointed", "unhelpful",
    }

    words = set(
        text.replace(".", " ").replace(",", " ").split()
    )
    positive = len(words & positive_words)
    negative = len(words & negative_words)

    if positive > negative:
        return {"label": "Positive", "icon": "😊"}
    if negative > positive:
        return {"label": "Negative", "icon": "☹️"}
    return {"label": "Neutral", "icon": "😐"}


SAMPLE_REVIEWS = {
    1: [
        {
            "id": 1,
            "dealership": 1,
            "name": "Alex",
            "review": "Excellent customer service and helpful staff.",
            "purchase": {
                "car_make": "Toyota",
                "car_model": "Camry",
                "car_year": 2024,
                "purchase_date": "2026-01-15",
            },
        },
        {
            "id": 2,
            "dealership": 1,
            "name": "Jordan",
            "review": "The buying process was smooth and easy.",
            "purchase": {
                "car_make": "Honda",
                "car_model": "Civic",
                "car_year": 2023,
                "purchase_date": "2026-02-10",
            },
        },
    ],
    2: [
        {
            "id": 3,
            "dealership": 2,
            "name": "Taylor",
            "review": "Good selection of cars.",
            "purchase": {
                "car_make": "Ford",
                "car_model": "Mustang",
                "car_year": 2024,
                "purchase_date": "2026-03-05",
            },
        },
    ],
    3: [
        {
            "id": 4,
            "dealership": 3,
            "name": "Morgan",
            "review": "Friendly staff and a good range of vehicles.",
            "purchase": {
                "car_make": "Toyota",
                "car_model": "Corolla",
                "car_year": 2022,
                "purchase_date": "2026-04-12",
            },
        },
        {
            "id": 5,
            "dealership": 3,
            "name": "Casey",
            "review": "The staff answered all my questions.",
            "purchase": {
                "car_make": "Honda",
                "car_model": "Accord",
                "car_year": 2023,
                "purchase_date": "2026-04-20",
            },
        },
    ],
    4: [
        {
            "id": 6,
            "dealership": 4,
            "name": "Riley",
            "review": "Helpful team and a smooth buying experience.",
            "purchase": {
                "car_make": "Honda",
                "car_model": "Accord",
                "car_year": 2023,
                "purchase_date": "2026-05-20",
            },
        },
        {
            "id": 7,
            "dealership": 4,
            "name": "Jamie",
            "review": "Good service and clear information about the cars.",
            "purchase": {
                "car_make": "Toyota",
                "car_model": "Corolla",
                "car_year": 2022,
                "purchase_date": "2026-06-02",
            },
        },
    ],
}


@require_GET
def get_dealer_reviews(request, dealer_id):
    reviews = SAMPLE_REVIEWS.get(dealer_id)

    if reviews is None:
        return JsonResponse(
            {"error": "No reviews found for this dealer ID."},
            status=404,
        )

    return JsonResponse(
        {"dealer_id": dealer_id, "reviews": reviews},
        status=200,
    )


@require_GET
def fetch_dealer_reviews(request, dealer_id):
    return get_dealer_reviews(request, dealer_id)


@require_http_methods(["GET", "POST"])
def post_review_page(request, dealer_id):
    from accounts.dealers import SAMPLE_DEALERS

    if not any(dealer["id"] == dealer_id for dealer in SAMPLE_DEALERS):
        return JsonResponse({"error": "Dealer not found."}, status=404)

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        review = request.POST.get("review", "").strip()

        if name and review:
            next_id = max(
                (
                    item["id"]
                    for items in SAMPLE_REVIEWS.values()
                    for item in items
                ),
                default=0,
            ) + 1

            SAMPLE_REVIEWS.setdefault(dealer_id, []).append({
                "id": next_id,
                "dealership": dealer_id,
                "name": name,
                "review": review,
                "purchase": {
                    "car_make": request.POST.get("car_make", ""),
                    "car_model": request.POST.get("car_model", ""),
                    "car_year": request.POST.get("car_year", ""),
                    "purchase_date": request.POST.get("purchase_date", ""),
                },
            })
            return redirect("get_dealer_reviews", dealer_id=dealer_id)

    return render(
        request,
        "accounts/post_review.html",
        {"dealer_id": dealer_id},
    )
