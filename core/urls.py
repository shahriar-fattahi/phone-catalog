from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("common.urls", namespace="common")),
    path("admin/", admin.site.urls),
    path("products/", include("products.urls", namespace="products")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
]

if "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
