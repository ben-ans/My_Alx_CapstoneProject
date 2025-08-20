from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingView


router = DefaultRouter()
router.register(r'bookings', BookingView)

urlpatterns = router.urls
