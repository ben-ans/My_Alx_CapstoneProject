from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Property,PropertyImage,PropertyVideo
from .serializers import PropertyImageSerializer, PropertyVideoSerializer, PropertySerializer

class PropertyView(viewsets.ModelViewSet):
    queryset = Property.objects.all().order_by('created_at')
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(landlord=self.request.user)
    

class PropertyImageView(viewsets.ModelViewSet):
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer
    permission_classes = [permissions.IsAuthenticated]


class PropertyVideoView(viewsets.ModelViewSet):
    queryset = PropertyVideo.objects.all()
    serializer_class = PropertyVideoSerializer
    permission_classes = [permissions.IsAuthenticated]