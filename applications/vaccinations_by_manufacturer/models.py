from django.db import models
from .managers import Vaccinations_by_manufacturer_manager

# Create your models here.


class Vaccinations_by_manufacturer(models.Model):
    """Model definition for Vaccinations_by_manufacturer."""

    location = models.CharField("Location", max_length=50)
    date = models.CharField("Date", max_length=15)
    vaccine = models.CharField("Vaccine", max_length=30)
    total_vaccinations = models.PositiveIntegerField("Total vaccinations")

    objects = Vaccinations_by_manufacturer_manager()

    class Meta:
        verbose_name = "Vaccinations_by_manufacturer"
        verbose_name_plural = "Vaccinations_by_manufacturers"

    """ def __str__(self):
        return self.date
        pass """
