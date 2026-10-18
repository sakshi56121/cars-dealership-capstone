from django.http import JsonResponse
from django.views.decorators.http import require_GET

SAMPLE_DEALERS = [
    {
        "id": 1,
        "full_name": "Sample Auto Center",
        "city": "Houston",
        "state": "Texas",
        "address": "100 Main Street",
        "zip": "77001",
        "phone": "555-0101",
    },
    {
        "id": 2,
        "full_name": "Demo Motors",
        "city": "Dallas",
        "state": "Texas",
        "address": "200 Oak Avenue",
        "zip": "75201",
        "phone": "555-0102",
    },
    {
        "id": 3,
        "full_name": "Example Car Sales",
        "city": "Austin",
        "state": "Texas",
        "address": "300 Lake Road",
        "zip": "73301",
        "phone": "555-0103",
    },
]


@require_GET
def get_all_dealers(request):
    return JsonResponse(SAMPLE_DEALERS, safe=False, status=200)


@require_GET
def get_dealer_by_id(request, dealer_id):
    dealer = next(
        (item for item in SAMPLE_DEALERS if item["id"] == dealer_id),
        None,
    )

    if dealer is None:
        return JsonResponse(
            {"error": "Dealer not found."},
            status=404,
        )

    return JsonResponse(dealer, status=200)
