from rest_framework import serializers
from .models import Flight, Reservation




class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = ( 'id','flightNumber','operationAirlines', 'arrivalCity', 'dateOfDeparture', 'estimatedTimeofDeparture')




