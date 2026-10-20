
from django.http import JsonResponse


CAR_MODELS = [
    {"id": 1, "make": "Toyota", "model": "Corolla"},
    {"id": 2, "make": "Toyota", "model": "Camry"},
    {"id": 3, "make": "Honda", "model": "Civic"},
    {"id": 4, "make": "Honda", "model": "Accord"},
    {"id": 5, "make": "Ford", "model": "Mustang"},
    {"id": 6, "make": "Ford", "model": "F-150"},
    {"id": 7, "make": "BMW", "model": "X3"},
    {"id": 8, "make": "BMW", "model": "X5"},
    {"id": 9, "make": "Audi", "model": "A4"},
    {"id": 10, "make": "Audi", "model": "Q5"},
    {"id": 11, "make": "Mercedes-Benz", "model": "C-Class"},
    {"id": 12, "make": "Mercedes-Benz", "model": "E-Class"},
    {"id": 13, "make": "Chevrolet", "model": "Malibu"},
    {"id": 14, "make": "Chevrolet", "model": "Equinox"},
    {"id": 15, "make": "Nissan", "model": "Altima"},
]


def get_all_car_makes(request):
    """Return available car makes and models."""
    return JsonResponse(CAR_MODELS, safe=False)
