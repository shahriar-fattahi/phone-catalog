from django.db import models
from django.utils.text import slugify
from django_lifecycle import BEFORE_SAVE, LifecycleModelMixin, hook

from common.models import COUNTRY, BaseModel


class Brand(LifecycleModelMixin, models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    country = models.CharField(max_length=2, choices=COUNTRY)

    @hook(BEFORE_SAVE)
    def set_slug(self):
        if not self.slug:
            self.slug = slugify(self.name)

    def __str__(self) -> str:
        return self.name


class Mobile(BaseModel):
    model = models.CharField(max_length=255, unique=True)
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=255)
    size_screen = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    manufacturer = models.CharField(max_length=2, choices=COUNTRY)
    brand = models.ForeignKey(
        to=Brand,
        on_delete=models.CASCADE,
        related_name="mobiles",
    )

    def __str__(self) -> str:
        self.model
