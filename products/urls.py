from django.urls import include, path

from .views import AddBrandView

app_name = "products"

brand_urls = [
    path("add", AddBrandView.as_view(), name="add-brand"),
]
product_urls = [
    path("add", AddBrandView.as_view(), name="add-brand"),
]

urlpatterns = [
    path("brands/", include(brand_urls)),
    path("products/", include(product_urls)),
]
