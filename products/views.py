from django.contrib import messages
from django.shortcuts import render
from django.views import View

from common.mixins import AdminRequiredMixin

from .forms import BrandForm, MobileForm


class AddBrandView(AdminRequiredMixin, View):
    template_name = "products/add_brand.html"
    form_class = BrandForm

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
            form.save()
            messages.success(
                request=request,
                message="Brand added successfuly",
            )
            context = {
                "form": self.form_class,
            }
            return render(
                request=request,
                template_name=self.template_name,
                context=context,
            )
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


class AddMobileView(AdminRequiredMixin, View):
    template_name = "products/add_mobile.html"
    form_class = MobileForm

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
            form.save()
            messages.success(
                request=request,
                message="Mobile added successfuly",
            )
            context = {
                "form": self.form_class,
            }
            return render(
                request=request,
                template_name=self.template_name,
                context=context,
            )
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
