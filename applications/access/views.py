from django.views.generic import View
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout


from django.urls import reverse_lazy, reverse
from django.http.response import HttpResponseRedirect

# from .models import Country_vaccinations
from .forms import (
    UserRegisterForm,
    LoginForm,
)
from .models import User


class UserLoginView(FormView):
    template_name = "access/sign-in.html"
    form_class = LoginForm
    success_url = reverse_lazy("country_vaccinations:by-country")

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        # if user is not None:
        login(self.request, user)
        return super(UserLoginView, self).form_valid(form)


class UserRegisterView(FormView):
    template_name = "access/sign-up.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("access:login")

    def form_valid(self, form):
        isAdmin = form.cleaned_data["isAdmin"]

        if isAdmin:
            # create superuser
            User.objects.create_superuser(
                form.cleaned_data["username"],
                form.cleaned_data["password"],
            )
        else:
            # create user
            User.objects.create_user(
                form.cleaned_data["username"],
                form.cleaned_data["password"],
            )

        return super(UserRegisterView, self).form_valid(form)


class UserLogoutView(View):
    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(reverse("access:login"))
