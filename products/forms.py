from django import forms
from django.core import validators
from django.utils.text import slugify

from .models import Brand, Mobile


class BrandForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control "

    class Meta:
        model = Brand
        fields = "__all__"

    def clean_slug(self):
        slug = self.cleaned_data.get("slug")
        if slug is None or slug == "":
            slug = slugify(self.cleaned_data["name"])
        if Brand.objects.filter(slug=slug).exists():
            raise forms.ValidationError(
                message=f"[{slug}] set as slug and brand with this slug is already exists"
            )
        return slug


class MobileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name == "is_available":
                visible.field.widget.attrs["class"] = "form-check-input "
            else:
                visible.field.widget.attrs["class"] = "form-control "

    class Meta:
        model = Mobile
        fields = "__all__"


class BrandSearchForm(forms.Form):
    brand = forms.CharField(max_length=255, required=True)
