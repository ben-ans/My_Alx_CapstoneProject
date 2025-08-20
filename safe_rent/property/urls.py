from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropertyView, PropertyImageView, PropertyVideoView

"""This single line creates all these routes behind the scenes:

GET /properties/ → list

POST /properties/ → create

GET /properties/{id}/ → retrieve

PUT /properties/{id}/ → update

PATCH /properties/{id}/ → partial update

DELETE /properties/{id}/ → delete
"""

router = DefaultRouter()
router.register(r'properties', PropertyView, basename='property')
router.register(r'property-images', PropertyImageView, basename='propertyimage')
router.register(r'property-videos', PropertyVideoView, basename='propertyvideo')

urlpatterns = [
    path('', include(router.urls)),
]
