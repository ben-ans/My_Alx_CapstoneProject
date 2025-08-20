from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionView


router = DefaultRouter()
router.register(r'transactions', TransactionView)

urlpatterns = router.urls
