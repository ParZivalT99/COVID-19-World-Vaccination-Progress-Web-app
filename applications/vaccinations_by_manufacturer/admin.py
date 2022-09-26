from django.contrib import admin
from .models import Vaccinations_by_manufacturer

# Register your models here.

class Vaccinations_by_manufacturer_admin(admin.ModelAdmin):
    list_display = ("id", "location", "date", "vaccine", "total_vaccinations")
    search_fields = ("id",)
    list_filter = (
        "location",
        "vaccine",
    )


admin.site.register(Vaccinations_by_manufacturer, Vaccinations_by_manufacturer_admin)
