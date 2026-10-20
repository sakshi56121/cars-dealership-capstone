from django.http import JsonResponse


def get_all_car_makes(request):
    car_models = [
        {"CarMake": {"Id": 1, "Name": "Toyota"}, "CarModel": {"Id": 1, "Name": "Camry"}},
        {"CarMake": {"Id": 1, "Name": "Toyota"}, "CarModel": {"Id": 2, "Name": "Corolla"}},
        {"CarMake": {"Id": 2, "Name": "Honda"}, "CarModel": {"Id": 3, "Name": "Civic"}},
        {"CarMake": {"Id": 2, "Name": "Honda"}, "CarModel": {"Id": 4, "Name": "Accord"}},
        {"CarMake": {"Id": 3, "Name": "Ford"}, "CarModel": {"Id": 5, "Name": "Mustang"}},
        {"CarMake": {"Id": 3, "Name": "Ford"}, "CarModel": {"Id": 6, "Name": "Focus"}},
        {"CarMake": {"Id": 4, "Name": "BMW"}, "CarModel": {"Id": 7, "Name": "3 Series"}},
        {"CarMake": {"Id": 4, "Name": "BMW"}, "CarModel": {"Id": 8, "Name": "5 Series"}},
        {"CarMake": {"Id": 5, "Name": "Mercedes-Benz"}, "CarModel": {"Id": 9, "Name": "C-Class"}},
        {"CarMake": {"Id": 5, "Name": "Mercedes-Benz"}, "CarModel": {"Id": 10, "Name": "E-Class"}},
        {"CarMake": {"Id": 6, "Name": "Audi"}, "CarModel": {"Id": 11, "Name": "A3"}},
        {"CarMake": {"Id": 6, "Name": "Audi"}, "CarModel": {"Id": 12, "Name": "A4"}},
        {"CarMake": {"Id": 7, "Name": "Hyundai"}, "CarModel": {"Id": 13, "Name": "Elantra"}},
        {"CarMake": {"Id": 7, "Name": "Hyundai"}, "CarModel": {"Id": 14, "Name": "Sonata"}},
        {"CarMake": {"Id": 8, "Name": "Kia"}, "CarModel": {"Id": 15, "Name": "Sportage"}},
    ]
    return JsonResponse({"CarModels": car_models})
