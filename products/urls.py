from django.urls import include, path

from .views import AddBrandView, AddMobileView, KoreanBrandListView

app_name = "products"

brand_urls = [
    path("add", AddBrandView.as_view(), name="add-brand"),
    path("korean", KoreanBrandListView.as_view(), name="korean-brands"),
]
product_urls = [
    path("add", AddMobileView.as_view(), name="add-mobile"),
]

urlpatterns = [
    path("brands/", include(brand_urls)),
    path("products/", include(product_urls)),
]
