from django.db import models

class Room(models.Model):
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Room {self.room_number} ({self.room_type})"

class RoomBooking(models.Model):
    user_id = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    status = models.CharField(choices=[('booked', 'Booked'), ('cancelled', 'Cancelled')], max_length=10)

    def __str__(self):
        return f"Booking for user {self.user_id} in room {self.room.id}"
