from email.utils import localtime
from django.shortcuts import render
from django.views.generic import ListView

from .models import Vaccinations_by_manufacturer


class HomeVaccinationsByManufacturerView(ListView):
    template_name = "vaccinations_by_manufacturer/home_vm.html"
    paginate_by = 30
    model = Vaccinations_by_manufacturer
    context_object_name = "bymanufacturer"

    def get(self, request, *args, **kwargs):

        if request.user.is_superuser:
            return super(HomeVaccinationsByManufacturerView, self).get(
                request, *args, **kwargs
            )
        else:
            return render(request, "access/permission-denied.html")

    def get_context_data(self, **kwargs):
        context = super(HomeVaccinationsByManufacturerView, self).get_context_data(
            **kwargs
        )
        location = self.request.GET.get("location")
        date = self.request.GET.get("date")
        vaccine = self.request.GET.get("vaccine")

        context["location"] = location
        context["date"] = date
        context["vaccine"] = vaccine
        return context

    def get_queryset(self):
        queryset = super(HomeVaccinationsByManufacturerView, self).get_queryset()
        location = self.request.GET.get("location")
        date = self.request.GET.get("date")
        vaccine = self.request.GET.get("vaccine")

        if location and date and vaccine:
            if queryset.filter(
                location__iexact=location, date=date, vaccine__iexact=vaccine
            ):
                queryset = queryset.filter(
                    location__iexact=location, date=date, vaccine__iexact=vaccine
                )

        elif location and date:
            if queryset.filter(location__iexact=location, date=date):
                queryset = queryset.filter(location__iexact=location, date=date)

        elif location and vaccine:
            if queryset.filter(location__iexact=location, vaccine__iexact=vaccine):
                queryset = queryset.filter(
                    location__iexact=location, vaccine__iexact=vaccine
                )

        elif date and vaccine:
            if queryset.filter(date=date, vaccine__iexact=vaccine):
                queryset = queryset.filter(date=date, vaccine__iexact=vaccine)

        elif location:
            if queryset.filter(location__iexact=location):
                queryset = queryset.filter(location__iexact=location)

        elif date:
            if queryset.filter(date=date):
                queryset = queryset.filter(date=date)

        elif vaccine:
            if queryset.filter(vaccine__iexact=vaccine):
                queryset = queryset.filter(vaccine__iexact=vaccine)

        return queryset
