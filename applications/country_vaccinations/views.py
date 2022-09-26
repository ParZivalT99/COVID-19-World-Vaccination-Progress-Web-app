from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.urls import reverse_lazy

from .models import Country_vaccinations


class HomeCountryVaccinationsView(LoginRequiredMixin, ListView):
    template_name = "country_vaccinations/home_cv.html"
    paginate_by = 30
    model = Country_vaccinations
    context_object_name = "country"
    login_url = reverse_lazy("access:login")

    def get_context_data(self, **kwargs):
        context = super(HomeCountryVaccinationsView, self).get_context_data(**kwargs)

        iso_code = self.request.GET.get("iso_code")
        date = self.request.GET.get("date")
        context["date"] = date
        context["iso_code"] = iso_code
        return context

    def get_queryset(self):
        queryset = super(HomeCountryVaccinationsView, self).get_queryset()
        iso_code = self.request.GET.get("iso_code")
        date = self.request.GET.get("date")

        if iso_code and date:
            if queryset.filter(iso_code__iexact=iso_code, date=date):
                queryset = queryset.filter(iso_code__iexact=iso_code, date=date)

        elif iso_code:
            if queryset.filter(iso_code__iexact=iso_code):
                queryset = queryset.filter(iso_code__iexact=iso_code)

        elif date:
            if queryset.filter(date=date):
                queryset = queryset.filter(date=date)

        return queryset
