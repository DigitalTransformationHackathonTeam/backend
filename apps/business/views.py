from rest_framework import generics

from business.models import Business
from business.serializers import BusinessSerializer


class BusinessesListView(generics.ListAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
