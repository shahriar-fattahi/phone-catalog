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
        print(self.cleaned_data)
        slug = self.cleaned_data.get("slug")
        if slug is None or slug == "":
            slug = slugify(self.cleaned_data["name"])
        if Brand.objects.filter(slug=slug).exists():
            print("err")
            raise forms.ValidationError(
                message=f"[{slug}] set as slug and brand with this slug is already exists"
            )
        return slug
