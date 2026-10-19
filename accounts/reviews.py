from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.views.decorators.http import require_GET

SAMPLE_REVIEWS = {
    1: [
        {
            "id": 1,
            "dealership": 1,
            "name": "Alex",
            "review": "Excellent customer service and helpful staff."
        },
        {
            "id": 2,
            "dealership": 1,
            "name": "Jordan",
            "review": "The buying process was smooth and easy."
        }
    ],
    2: [
        {
            "id": 3,
            "dealership": 2,
            "name": "Taylor",
            "review": "Good selection of cars."
        }
    ],
    3: [
        {
            "id": 4,
            "dealership": 3,
            "name": "Morgan",
            "review": "Friendly staff and a good range of vehicles."
        },
        {
            "id": 5,
            "dealership": 3,
            "name": "Casey",
            "review": "The staff answered all my questions."
        }
    ],
    4: [
        {
            "id": 6,
            "dealership": 4,
            "name": "Riley",
            "review": "Helpful team and a smooth buying experience."
        },
        {
            "id": 7,
            "dealership": 4,
            "name": "Jamie",
            "review": "Good service and clear information about the cars."
        }
    ]
}


@require_GET
def get_dealer_reviews(request, dealer_id):
    reviews = SAMPLE_REVIEWS.get(dealer_id)

    if reviews is None:
        return JsonResponse(
            {"error": "No reviews found for this dealer ID."},
            status=404
        )

    return JsonResponse(
        {"dealer_id": dealer_id, "reviews": reviews},
        status=200
    )


@require_http_methods(["GET", "POST"])
def post_review_page(request, dealer_id):
    if not any(dealer["id"] == dealer_id for dealer in __import__(
        "accounts.dealers", fromlist=["SAMPLE_DEALERS"]
    ).SAMPLE_DEALERS):
        return JsonResponse({"error": "Dealer not found."}, status=404)

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        review = request.POST.get("review", "").strip()

        if name and review:
            SAMPLE_REVIEWS.setdefault(dealer_id, []).append({
                "id": max(
                    (
                        item["id"]
                        for items in SAMPLE_REVIEWS.values()
                        for item in items
                    ),
                    default=0,
                ) + 1,
                "dealership": dealer_id,
                "name": name,
                "review": review,
            })
            return redirect("get_dealer_reviews", dealer_id=dealer_id)

    return render(
        request,
        "accounts/post_review.html",
        {"dealer_id": dealer_id},
    )
