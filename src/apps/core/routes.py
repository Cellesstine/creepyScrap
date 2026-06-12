from django.urls import path
from .views import netInterface, networkManager

urlpatterns = [
	path("", netInterface, name="networkManager"),
	path("creepyScrap/", networkManager, name="creepyScrap"),
]