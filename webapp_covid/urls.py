from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("applications.access.urls")),
    path(
        "dashboard/vaccinations-by-manufacturer/",
        include("applications.vaccinations_by_manufacturer.urls"),
    ),
    path(
        "dashboard/vaccinations-by-country/",
        include("applications.country_vaccinations.urls"),
    ),
    path("api/v1/", include("applications.api.urls")),
]
