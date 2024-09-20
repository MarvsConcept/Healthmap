from django.shortcuts import render
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Hospital

def home(request):
    return render(request, 'hospitals/home.html')

def hospitals_list(request):
    longitude = float(request.GET.get('lon', 5.1951))
    latitude = float(request.GET.get('lat', 7.2571))
    page = int(request.GET.get('page', 1))
    per_page = int(request.GET.get('per_page', 10))

    user_location = Point(longitude, latitude, srid=4326)

    hospitals = Hospital.objects.annotate(
        distance=Distance('location', user_location)
    ).order_by('distance')

    paginator = Paginator(hospitals, per_page)
    page_obj = paginator.get_page(page)

    hospital_data = [{
        'id': hospital.id,
        'name': hospital.name,
        'address': hospital.address,
        'latitude': hospital.latitude,
        'longitude': hospital.longitude,
        'amenity': hospital.amenity,
        'opening_hours': hospital.opening_hours,
        'image': hospital.image.url if hospital.image else None,
        'number': hospital.number,
        'rating': hospital.rating,
        'distance': round(hospital.distance.km, 2)
    } for hospital in page_obj]

    print(hospital_data)  # Print data to ensure it's being retrieved correctly

    response_data = {
        'hospitals': hospital_data,
        'total_pages': paginator.num_pages,
        'current_page': page,
        'total_items': paginator.count
    }

    return JsonResponse(response_data)