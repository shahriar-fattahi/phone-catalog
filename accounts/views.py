from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from .forms import LoginForm


class LoginView(View):
    template_name = "accounts/login.html"
    form_class = LoginForm

    def get(self, request):
        context = {
            "form": self.form_class,
        }
        return render(
            request=request,
            template_name=self.template_name,
            context=context,
        )

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(
                request,
                username=username,
                password=password,
            )
            if user is None or user.is_admin is False:
                messages.warning(request, "The username or password is incorrect")
                return redirect(to=request.META.get("HTTP_REFERER"))
            messages.success(request, "You logged in successfully")
            next = request.GET.get("next", reverse("common:home"))
            login(
                request=request,
                user=user,
                backend="django.contrib.auth.backends.ModelBackend",
            )
            return redirect(to=next)

        for field in form.errors:
            form[field].field.widget.attrs["class"] += " is-invalid "
        context = {
            "form": form,
        }
        return render(
            request=request,
            template_name=self.template_name,
            context=context,
        )


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request=request)
        return redirect(to=reverse("common:home"))
