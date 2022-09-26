from rest_framework import serializers, pagination

from ..country_vaccinations.models import Country_vaccinations
from ..vaccinations_by_manufacturer.models import Vaccinations_by_manufacturer


class CountryVaccinationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country_vaccinations
        fields = "__all__"


class VaccinationsByManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccinations_by_manufacturer
        fields = "__all__"


class VaccinationsPagination(pagination.PageNumberPagination):
    page_size = 20
    max_page_size = 50
