from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'doctor', views.DoctorView)
router.register(r'direction', views.DirectionView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
