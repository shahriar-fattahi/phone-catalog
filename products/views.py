from django.contrib import messages
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from common.mixins import AdminRequiredMixin
from common.models import COUNTRY

from .forms import BrandForm, MobileForm
from .models import Brand, Mobile


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


class KoreanBrandListView(ListView):
    template_name = "products/brand_list.html"
    context_object_name = "objects"
    model = Brand

    def get_queryset(self):
        return self.model.objects.filter(country=COUNTRY.KR)
