from django.urls import path
from .views import RideList, BookingList, CreateBooking  # Ensure CreateBooking is imported

urlpatterns = [
    path('rides/', RideList.as_view(), name='ride-list'),
    path('bookings/', BookingList.as_view(), name='booking-list'),
    path('bookings/create/', CreateBooking.as_view(), name='create-booking'),  # New URL for creating a booking
]


