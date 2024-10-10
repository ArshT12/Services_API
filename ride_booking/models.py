from django.db import models

class Ride(models.Model):
    pickup_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    vehicle_type = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Ride from {self.pickup_location} to {self.destination}"

class Booking(models.Model):
    user_id = models.IntegerField()
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    status = models.CharField(choices=[('booked', 'Booked'), ('cancelled', 'Cancelled')], max_length=10)

    def __str__(self):
        return f"Booking for user {self.user_id} on ride {self.ride.id}"
