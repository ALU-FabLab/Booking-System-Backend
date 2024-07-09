from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventory.views import EquipmentViewSet

router = DefaultRouter()
router.register('equipments', EquipmentViewSet)

app_name = 'inventory'

urlpatterns = [
    path('', include(router.urls))
]
