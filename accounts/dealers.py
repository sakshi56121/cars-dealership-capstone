
from django.http import JsonResponse
from django.views.decorators.http import require_GET

CITIES = [
    ("Houston", "Texas", "77001", 29.7604, -95.3698),
    ("Dallas", "Texas", "75201", 32.7767, -96.7970),
    ("Austin", "Texas", "73301", 30.2672, -97.7431),
    ("Wichita", "Kansas", "67202", 37.6872, -97.3301),
    ("New York", "New York", "10001", 40.7128, -74.0060),
    ("Los Angeles", "California", "90001", 34.0522, -118.2437),
    ("Chicago", "Illinois", "60601", 41.8781, -87.6298),
    ("Phoenix", "Arizona", "85001", 33.4484, -112.0740),
    ("Philadelphia", "Pennsylvania", "19103", 39.9526, -75.1652),
    ("San Antonio", "Texas", "78205", 29.4241, -98.4936),
]

SAMPLE_DEALERS = []

for dealer_id in range(1, 51):
    city, state, zip_code, lat, long = CITIES[(dealer_id - 1) % len(CITIES)]

    SAMPLE_DEALERS.append({
        "id": dealer_id,
        "full_name": f"{city} Auto Center {dealer_id}",
        "short_name": f"Dealer {dealer_id}",
        "city": city,
        "state": state,
        "address": f"{100 + dealer_id} Main Street",
        "zip": zip_code,
        "phone": f"555-{dealer_id:04d}",
        "lat": lat,
        "long": long,
    })


@require_GET
def get_all_dealers(request):
    return JsonResponse(SAMPLE_DEALERS, safe=False, status=200)


@require_GET
def fetch_dealers(request):
    return get_all_dealers(request)


@require_GET
def get_dealer_by_id(request, dealer_id):
    dealer = next(
        (item for item in SAMPLE_DEALERS if item["id"] == dealer_id),
        None,
    )

    if dealer is None:
        return JsonResponse({"error": "Dealer not found."}, status=404)

    return JsonResponse(dealer, status=200)


@require_GET
def get_dealers_by_state(request):
    state = request.GET.get("state", "").strip()

    if not state:
        return JsonResponse(
            {"error": "Please provide a state query parameter."},
            status=400,
        )

    dealers = [
        dealer for dealer in SAMPLE_DEALERS
        if dealer["state"].lower() == state.lower()
    ]

    return JsonResponse(dealers, safe=False, status=200)
