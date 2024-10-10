from django.urls import path
from .views import RoomList, RoomBookingList, CreateRoomBooking, CancelRoomBooking

urlpatterns = [
    path('rooms/', RoomList.as_view(), name='room-list'),
    path('bookings/', RoomBookingList.as_view(), name='room-booking-list'),
    path('bookings/create/', CreateRoomBooking.as_view(), name='create-room-booking'),
    path('bookings/cancel/<int:booking_id>/', CancelRoomBooking.as_view(), name='cancel-room-booking'),
]
