from django.urls import include, path

from .views import AddBrandView, AddMobileView, KoreanBrandListView, SeachMobileView

app_name = "products"

brand_urls = [
    path("add", AddBrandView.as_view(), name="add-brand"),
    path("korean", KoreanBrandListView.as_view(), name="korean-brands"),
]
mobile_urls = [
    path("add", AddMobileView.as_view(), name="add-mobile"),
    path("search/", SeachMobileView.as_view(), name="search-mobile"),
]

urlpatterns = [
    path("brands/", include(brand_urls)),
    path("mobiles/", include(mobile_urls)),
]
