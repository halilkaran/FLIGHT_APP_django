from .models import Flight, Reservation
from .serializers import FlightSerializer
from rest_framework import viewsets
from .permissions import IsStufforReadOnly

class FlightView(viewsets.ModelViewSet): # GET POST UPDATE DELETE viewset sayesinde
    queryset= Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsStufforReadOnly,)



