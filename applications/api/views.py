from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status

from ..country_vaccinations.models import Country_vaccinations
from ..vaccinations_by_manufacturer.models import Vaccinations_by_manufacturer

from .serializers import (
    CountryVaccinationsSerializer,
    VaccinationsByManufacturerSerializer,
    VaccinationsPagination,
)


class CountryVaccinationsRetrieveAPIView(RetrieveAPIView):
    queryset = Country_vaccinations.objects.all()
    serializer_class = CountryVaccinationsSerializer


class VaccinationsManufacturerRetrieveAPIView(RetrieveAPIView):
    queryset = Vaccinations_by_manufacturer.objects.all()
    serializer_class = VaccinationsByManufacturerSerializer


class CountryVaccinationsListAPIView(ListAPIView):

    queryset = Country_vaccinations.objects.all()
    serializer_class = CountryVaccinationsSerializer
    pagination_class = VaccinationsPagination


class VaccinationsManufacturerListAPIView(ListAPIView):

    queryset = Vaccinations_by_manufacturer.objects.all()
    serializer_class = VaccinationsByManufacturerSerializer
    pagination_class = VaccinationsPagination


class VaccinationsByIsoCodeListAPIView(ListAPIView):

    queryset = Country_vaccinations.objects.all()
    serializer_class = CountryVaccinationsSerializer
    pagination_class = VaccinationsPagination

    def get(self, request, *args, **kwargs):

        if self.get_queryset():
            return super(VaccinationsByIsoCodeListAPIView, self).get(
                request, *args, **kwargs
            )
        else:
            return Response(
                {"bad request": "Wrong iso code"}, status=status.HTTP_400_BAD_REQUEST
            )

    def get_queryset(self):
        queryset = super(VaccinationsByIsoCodeListAPIView, self).get_queryset()
        iso_code = self.kwargs["iso_code_pk"]
        queryset = queryset.filter(iso_code__iexact=iso_code)

        return queryset


class VaccinationsByDateListAPIView(ListAPIView):

    queryset = Country_vaccinations.objects.all()
    serializer_class = CountryVaccinationsSerializer
    pagination_class = VaccinationsPagination

    def get(self, request, *args, **kwargs):

        if self.get_queryset():
            return super(VaccinationsByDateListAPIView, self).get(
                request, *args, **kwargs
            )
        else:
            return Response(
                {"bad request": "Wrong date"}, status=status.HTTP_400_BAD_REQUEST
            )

    def get_queryset(self):
        queryset = super(VaccinationsByDateListAPIView, self).get_queryset()
        date = self.kwargs["date_pk"]
        queryset = queryset.filter(date=date)

        return queryset


class VaccinationsByIsoCodeAndDateListAPIView(ListAPIView):

    queryset = Country_vaccinations.objects.all()
    serializer_class = CountryVaccinationsSerializer
    pagination_class = VaccinationsPagination

    def get(self, request, *args, **kwargs):

        if self.get_queryset():
            return super(VaccinationsByIsoCodeAndDateListAPIView, self).get(
                request, *args, **kwargs
            )
        else:
            return Response(
                {"bad request": "Wrong parameters"}, status=status.HTTP_400_BAD_REQUEST
            )

    def get_queryset(self):
        queryset = super(VaccinationsByIsoCodeAndDateListAPIView, self).get_queryset()

        iso_code = self.kwargs["iso_code_pk"]
        iso_code = iso_code.upper()
        date = self.kwargs["date_pk"]

        queryset = queryset.filter(iso_code__iexact=iso_code, date=date)

        return queryset


class VaccinationsByLocationListAPIView(ListAPIView):

    queryset = Vaccinations_by_manufacturer.objects.all()
    serializer_class = VaccinationsByManufacturerSerializer
    pagination_class = VaccinationsPagination

    def get(self, request, *args, **kwargs):

        if self.get_queryset():
            return super(VaccinationsByLocationListAPIView, self).get(
                request, *args, **kwargs
            )
        else:
            return Response(
                {"bad request": "Wrong location"}, status=status.HTTP_400_BAD_REQUEST
            )

    def get_queryset(self):
        queryset = super(VaccinationsByLocationListAPIView, self).get_queryset()
        location = self.kwargs["location_pk"]
        queryset = queryset.filter(location__iexact=location)

        return queryset


class VaccinationsBymDateListAPIView(ListAPIView):

    queryset = Vaccinations_by_manufacturer.objects.all()
    serializer_class = VaccinationsByManufacturerSerializer
    pagination_class = VaccinationsPagination

    def get(self, request, *args, **kwargs):

        if self.get_queryset():
            return super(VaccinationsBymDateListAPIView, self).get(
                request, *args, **kwargs
            )
        else:
            return Response(
                {"bad request": "Wrong date"}, status=status.HTTP_400_BAD_REQUEST
            )

    def get_queryset(self):
        queryset = super(VaccinationsBymDateListAPIView, self).get_queryset()
        date = self.kwargs["date_pk"]
        queryset = queryset.filter(date=date)

        return queryset


class VaccinationsByVaccineListAPIView(ListAPIView):

    queryset = Vaccinations_by_manufacturer.objects.all()
    serializer_class = VaccinationsByManufacturerSerializer
    pagination_class = VaccinationsPagination

    def get(self, request, *args, **kwargs):

        if self.get_queryset():
            return super(VaccinationsByVaccineListAPIView, self).get(
                request, *args, **kwargs
            )
        else:
            return Response(
                {"bad request": "Wrong vaccine"}, status=status.HTTP_400_BAD_REQUEST
            )

    def get_queryset(self):
        queryset = super(VaccinationsByVaccineListAPIView, self).get_queryset()
        vaccine = self.kwargs["vaccine_pk"]
        queryset = queryset.filter(vaccine__iexact=vaccine)

        return queryset


class VaccinationsBylocationDateVaccineListAPIView(ListAPIView):

    queryset = Vaccinations_by_manufacturer.objects.all()
    serializer_class = VaccinationsByManufacturerSerializer
    pagination_class = VaccinationsPagination

    def get(self, request, *args, **kwargs):

        if self.get_queryset():
            return super(VaccinationsBylocationDateVaccineListAPIView, self).get(
                request, *args, **kwargs
            )
        else:
            return Response(
                {"bad request": "Wrong parameters"}, status=status.HTTP_400_BAD_REQUEST
            )

    def get_queryset(self):
        queryset = super(
            VaccinationsBylocationDateVaccineListAPIView, self
        ).get_queryset()
        location = self.kwargs["location_pk"]
        date = self.kwargs["date_pk"]
        vaccine = self.kwargs["vaccine_pk"]

        queryset = queryset.filter(
            location__iexact=location, date=date, vaccine__iexact=vaccine
        )

        return queryset
