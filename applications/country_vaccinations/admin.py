from django.contrib import admin
from .models import Country_vaccinations


class Country_vaccinations_admin(admin.ModelAdmin):
    list_display = (
        "id",
        "date",
        "iso_code",
        "total_vaccinations",
        "vaccines",
    )
    search_fields = ("iso_code",)
    list_filter = ("iso_code",)


admin.site.register(Country_vaccinations, Country_vaccinations_admin)
