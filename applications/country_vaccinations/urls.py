from django.urls import path, include
from . import views

app_name = "country_vaccinations"

urlpatterns = [
    path("", views.HomeCountryVaccinationsView.as_view(), name="by-country"),
]
