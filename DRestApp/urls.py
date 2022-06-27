from django.urls import path, include
from rest_framework import routers
from .views import EmployeeViewSet
from DRestApp import views

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
