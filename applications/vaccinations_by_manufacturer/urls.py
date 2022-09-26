from django.urls import path
from . import views

app_name = "vaccinations_by_manufacturer"

urlpatterns = [
    
    path(
        "",
        views.HomeVaccinationsByManufacturerView.as_view(),
        name="by-manufacturer",
    ),
]
