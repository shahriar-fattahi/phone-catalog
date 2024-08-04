from django.test import Client, TestCase
from django.urls import reverse

from accounts.models import User

from ..models import Brand, Mobile
from .model_factory import BranFactory, MobileFactory


class TestAddBrandView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin = User.objects.create_superuser(
            username="testadmin",
            email="testadmin@test.com",
            phone="09122222222",
            password="123",
            first_name="test",
            last_name="admin",
        )
        self.non_admin = User.objects.create_user(
            username="non_admintest",
            email="non_admintest@test.com",
            phone="09133333333",
            password="123",
            first_name="test",
            last_name="non_admin",
        )
        return super().setUp()

    def test_view_permmisions(self):
        response = self.client.get(path=reverse("products:add-brand"))
        self.assertEqual(
            response.status_code, 302
        )  # redirect status code for anonymous user
        self.assertEqual(response.url, "/accounts/login/?next=/products/brands/add")

        self.client.login(username="testadmin", password="123")
        response = self.client.get(path=reverse("products:add-brand"))
        self.assertEqual(response.status_code, 200)  # ok status code for admin user

        self.client.login(username="non_admintest", password="123")
        response = self.client.get(path=reverse("products:add-brand"))
        self.assertEqual(
            response.status_code, 403
        )  # forbidden status code for non admin user

    def test_add_new_brand(self):
        self.client.login(username="testadmin", password="123")
        response = self.client.post(
            reverse("products:add-brand"),
            {
                "name": "TEST BRAND",
                "country": "KR",
            },
        )
        self.assertEqual(response.status_code, 200)
        brand = Brand.objects.filter(name="TEST BRAND")
        self.assertEqual(brand.count(), 1)
        self.assertEqual(brand[0].slug, "test-brand")
        self.assertEqual(brand[0].country, "KR")


class TestAddMobileView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin = User.objects.create_superuser(
            username="testadmin",
            email="testadmin@test.com",
            phone="09122222222",
            password="123",
            first_name="test",
            last_name="admin",
        )
        self.non_admin = User.objects.create_user(
            username="non_admintest",
            email="non_admintest@test.com",
            phone="09133333333",
            password="123",
            first_name="test",
            last_name="non_admin",
        )
        return super().setUp()

    def test_view_permmisions(self):
        response = self.client.get(path=reverse("products:add-mobile"))
        self.assertEqual(
            response.status_code, 302
        )  # redirect status code for anonymous user
        self.assertEqual(response.url, "/accounts/login/?next=/products/mobiles/add")

        self.client.login(username="testadmin", password="123")
        response = self.client.get(path=reverse("products:add-mobile"))
        self.assertEqual(response.status_code, 200)  # ok status code for admin user

        self.client.login(username="non_admintest", password="123")
        response = self.client.get(path=reverse("products:add-mobile"))
        self.assertEqual(
            response.status_code, 403
        )  # forbidden status code for non admin user

    def test_add_new_brand(self):
        self.client.login(username="testadmin", password="123")
        brand = Brand.objects.create(name="TEST BRAND", country="KR")
        response = self.client.post(
            reverse("products:add-mobile"),
            {
                "model": "TEST MODEL",
                "price": 12,
                "color": "RED",
                "size_screen": 13,
                "manufacturer": "KR",
                "brand": brand.id,
            },
        )
        self.assertEqual(response.status_code, 200)
        mobile = Mobile.objects.filter(model="TEST MODEL")
        self.assertEqual(mobile.count(), 1)
        self.assertEqual(mobile[0].price, 12)
        self.assertEqual(mobile[0].color, "RED")
        self.assertEqual(mobile[0].size_screen, 13)
        self.assertEqual(mobile[0].manufacturer, "KR")
        self.assertEqual(mobile[0].brand.name, "TEST BRAND")
        self.assertEqual(mobile[0].brand.slug, "test-brand")
        self.assertEqual(mobile[0].brand.id, brand.id)


class TestKoreanBrandView(TestCase):
    def setUp(self) -> None:
        self.url = reverse("products:korean-brands")
        self.client = Client()
        self.korean_brands = BranFactory.create(name="bkr", country="KR")
        self.non_korean_brands = BranFactory.create(name="nbkr", country="AF")
        return super().setUp()

    def test_context_objects(self):
        response = self.client.get(path=self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["objects"].count(), 1)
        self.assertEqual(response.context["objects"][0].name, "bkr")


class TestTheSameCountryMobileView(TestCase):
    def setUp(self) -> None:
        self.url = reverse("products:the-same-country-mobiles")
        self.client = Client()
        self.brand1 = BranFactory.create(name="Brand1", country="KR")
        self.brand2 = BranFactory.create(name="Brand2", country="AF")
        self.mobile1 = MobileFactory.create(
            model="Mobile1", manufacturer="AF", brand=self.brand1
        )
        self.mobile2 = MobileFactory.create(
            model="Mobile2", manufacturer="AF", brand=self.brand2
        )
        return super().setUp()

    def test_context_objects(self):
        response = self.client.get(path=self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["mobiles"].count(), 1)
        self.assertEqual(response.context["mobiles"][0].model, "Mobile2")


class TestSeachMobileView(TestCase):
    def setUp(self) -> None:
        self.url = reverse("products:search-mobile")
        self.client = Client()
        self.brand1 = BranFactory.create(name="Brand1", country="KR")
        self.brand2 = BranFactory.create(name="Brand2", country="KR")
        self.mobile1 = MobileFactory.create(
            model="Mobile1", manufacturer="AF", brand=self.brand1
        )
        self.mobile2 = MobileFactory.create(
            model="Mobile2", manufacturer="AF", brand=self.brand2
        )
        return super().setUp()

    def test_context_objects(self):
        response = self.client.get(path=f"{self.url}?brand=Brand1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["mobiles"].count(), 1)
        self.assertEqual(response.context["mobiles"][0].model, "Mobile1")
