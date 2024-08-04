import factory


class BranFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "products.Brand"


class MobileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "products.Mobile"

    color = "RED"
    price = 12
    size_screen = 13
