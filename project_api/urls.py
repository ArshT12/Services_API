from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ride_booking/', include('ride_booking.urls')),  # Include the ride_booking app
    path('room_booking/', include('room_booking.urls')),
    path('online_ordering/', include('online_ordering.urls')), 
]

