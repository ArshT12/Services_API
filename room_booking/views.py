from django.http import JsonResponse
from django.views import View
from .models import Room, RoomBooking
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

class RoomList(View):
    def get(self, request):
        rooms = Room.objects.all().values()
        return JsonResponse(list(rooms), safe=False)

class RoomBookingList(View):
    def get(self, request):
        bookings = RoomBooking.objects.all().values()
        return JsonResponse(list(bookings), safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class CreateRoomBooking(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            room_id = data.get('room_id')
            user_id = data.get('user_id')
            room = Room.objects.get(id=room_id)

            booking = RoomBooking.objects.create(
                user_id=user_id,
                room=room,
                status='booked'
            )

            return JsonResponse({'message': 'Room booking created successfully!', 'booking_id': booking.id})
        except Room.DoesNotExist:
            return JsonResponse({'error': 'Room not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class CancelRoomBooking(View):
    def post(self, request, booking_id):
        try:
            booking = RoomBooking.objects.get(id=booking_id)
            booking.status = 'cancelled'
            booking.save()

            return JsonResponse({'message': 'Booking cancelled successfully!'})
        except RoomBooking.DoesNotExist:
            return JsonResponse({'error': 'Booking not found.'}, status=404)
