from django.http import JsonResponse
from django.views import View
from .models import Ride, Booking
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .models import Ride, Booking

class RideList(View):
    def get(self, request):
        rides = Ride.objects.all().values()  # Fetch all rides
        return JsonResponse(list(rides), safe=False)

class BookingList(View):
    def get(self, request):
        bookings = Booking.objects.all().values()  # Fetch all bookings
        return JsonResponse(list(bookings), safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CreateBooking(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            ride_id = data.get('ride_id')
            user_id = data.get('user_id')
            ride = Ride.objects.get(id=ride_id)
            
            booking = Booking.objects.create(
                user_id=user_id,
                ride=ride,
                status='booked'
            )
            
            return JsonResponse({'message': 'Booking created successfully!', 'booking_id': booking.id})
        except Ride.DoesNotExist:
            return JsonResponse({'error': 'Ride not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
