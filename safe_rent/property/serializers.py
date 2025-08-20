from rest_framework import serializers
from .models import Property, PropertyImage, PropertyVideo

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['id', 'image']


class PropertyVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyVideo
        fields = ['id', 'video']


class PropertySerializer(serializers.ModelSerializer):
    images = PropertyImageSerializer(many=True, read_only=True)
    videos = PropertyVideoSerializer(many=True, read_only=True)
    landlord = serializers.ReadOnlyField(source="landlord.username")

    class Meta:
        model = Property
        fields = [
            'id',
            'title',
            'description',
            'property_type',
            'location',
            'price',
            'available',
            'landlord',
            'images',
            'videos',
            'created_at',
        ]
