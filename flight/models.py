import email
from django.db import models
from django.contrib.auth.models import User

class Flight(models.Model):
    flightNumber=models.CharField(max_length=15)
    operationAirlines= models.CharField(max_length=15)
    departureCity= models.CharField(max_length=30)
    arrivalCity= models.CharField(max_length=30)
    dateOfDeparture= models.DateField()
    estimatedTimeofDeparture= models.TimeField()

    def __str__(self):
        return f' {self.flightNumber} - {self.departureCity} - {self.arrivalCity}'

class Passenger(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=40)
    email= models.EmailField()
    phone_Number= models.IntegerField()
    create_date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' {self.first_name} - {self.last_name}'

class Reservation(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    passenger=models.ManyToManyField(Passenger, related_name='passengers')
    flight= models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='reservations')
    
