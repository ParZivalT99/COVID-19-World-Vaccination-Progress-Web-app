from django.db import models
from .managers import Country_vaccinations_manager


class Country_vaccinations(models.Model):
    """Model definition for Country_vaccinations."""

    country = models.CharField("Country", max_length=50)
    iso_code = models.CharField("Iso code", max_length=20)
    date = models.CharField("Date", max_length=15)
    total_vaccinations = models.FloatField("Total vaccinations", max_length=50)
    people_vaccinated = models.FloatField("People vaccinated", max_length=50)
    people_fully_vaccinated = models.FloatField(
        "People fully vaccinated", max_length=50
    )
    daily_vaccinations_raw = models.FloatField("Daily vaccinations raw", max_length=50)
    daily_vaccinations = models.FloatField("Daily vaccinations", max_length=50)
    total_vaccinations_per_hundred = models.FloatField(
        "Total vaccinations per hundred", max_length=50
    )
    people_vaccinated_per_hundred = models.FloatField(
        "People vaccinated per hundred", max_length=50
    )
    people_fully_vaccinated_per_hundred = models.FloatField(
        "People fully vaccinated per hundred", max_length=50
    )
    daily_vaccinations_per_million = models.FloatField(
        "Daily vaccinations per million", max_length=50
    )
    vaccines = models.CharField("vaccines", max_length=150)
    source_name = models.CharField("source_name", max_length=80)

    objects = Country_vaccinations_manager()

    class Meta:
        verbose_name = "Country_vaccination"
        verbose_name_plural = "Country_vaccinations"
