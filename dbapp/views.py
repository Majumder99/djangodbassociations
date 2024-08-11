from django.http import JsonResponse
from django.views.generic import View
from .models import *

class PersonDetailView(View):
    def get(self, request, *args, **kwargs):
        try:
            # Fetch the person by ID
            person = Person.objects.get(pk=5)
            
            # Prepare the person's interests
            interests = list(person.interests.values('title'))
            
            # Fetch the person's address and city if available
            try:
                address = PersonAddress.objects.get(person=person)
                address_data = {
                    'street_address': address.street_address,
                    'city': address.city.title
                }
            except PersonAddress.DoesNotExist:
                address_data = {}
            
            # Preparing the JSON data
            data = {
                'name': person.name,
                'mobile': person.mobile,
                'interests': interests,
                'address': address_data
            }
            
            return JsonResponse(data, safe=False)
        except Person.DoesNotExist:
            return JsonResponse({'error': 'Person not found'}, status=404)


class PersonsInCityView(View):
    def get(self, request, *args, **kwargs):
        try:
            # Fetch the city by ID
            city = City.objects.get(pk=6)
            
            # Fetch all addresses in the city
            addresses = PersonAddress.objects.filter(city=city)
            print(addresses)
            
            # Collect all persons details
            persons_data = []
            for address in addresses:
                person = address.person
                interests = list(person.interests.values('title'))
                persons_data.append({
                    'name': person.name,
                    'mobile': person.mobile,
                    'interests': interests,
                    'street_address': address.street_address
                })
            
            data = {
                'city': city.title,
                'persons': persons_data
            }
            
            return JsonResponse(data, safe=False)
        except City.DoesNotExist:
            return JsonResponse({'error': 'City not found'}, status=404)