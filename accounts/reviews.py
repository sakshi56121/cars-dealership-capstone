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
