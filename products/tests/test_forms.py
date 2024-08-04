from django.test import TestCase

from ..forms import BrandForm, MobileForm
from ..models import Brand, Mobile


class TestBrandForm(TestCase):
    def setUp(self) -> None:
        self.data1 = {
            "name": "Brand Test1",
            "country": "KR",
        }
        self.data2 = {
            "name": "Brand Test2",
            "slug": "bt2",
            "country": "KR",
        }
        return super().setUp()

    def test_valid_data_without_slug(self):
        form = BrandForm(data=self.data1)
        self.assertTrue(form.is_valid())
        form.save()
        brand = Brand.objects.filter(name="Brand Test1")
        self.assertEqual(brand.count(), 1)
        self.assertEqual(brand[0].slug, "brand-test1")
        self.assertEqual(brand[0].country, "KR")

    def test_valid_data_with_slug(self):
        form = BrandForm(data=self.data2)
        self.assertTrue(form.is_valid())
        form.save()
        brand = Brand.objects.filter(name="Brand Test2")
        self.assertEqual(brand.count(), 1)
        self.assertEqual(brand[0].slug, "bt2")
        self.assertEqual(brand[0].country, "KR")

    def test_invalid_data(self):
        Brand.objects.create(**self.data1)
        form = BrandForm(data=self.data1)
        self.assertFalse(form.is_valid())
        self.assertRaises(ValueError, form.save)
        self.assertEqual(
            form.errors.get("name")[0],
            "Brand with this Name already exists.",
        )
        self.assertEqual(
            form.errors.get("slug")[0],
            "[brand-test1] set as slug and brand with this slug is already exists",
        )


class TestMobileForm(TestCase):
    def setUp(self) -> None:
        self.data_brand = {
            "name": "Brand Test",
            "slug": "bt",
            "country": "KR",
        }
        self.brand = Brand.objects.create(**self.data_brand)
        self.data_mobile = {
            "model": "Mobile Test1",
            "price": 12,
            "color": "RED",
            "size_screen": 13,
            "manufacturer": "KR",
            "brand": self.brand,
        }

        return super().setUp()

    def test_valid_data(self):
        form = MobileForm(data=self.data_mobile)
        self.assertTrue(form.is_valid())
        form.save()
        mobile = Mobile.objects.filter(model="Mobile Test1")
        self.assertEqual(mobile.count(), 1)
        self.assertEqual(mobile[0].price, 12)
        self.assertEqual(mobile[0].color, "RED")
        self.assertEqual(mobile[0].size_screen, 13)
        self.assertEqual(mobile[0].manufacturer, "KR")
        self.assertEqual(mobile[0].brand.name, "Brand Test")
        self.assertEqual(mobile[0].brand.slug, "bt")
        self.assertEqual(mobile[0].brand.id, self.brand.id)

    def test_invalid_data(self):
        Mobile.objects.create(**self.data_mobile)
        form = MobileForm(data=self.data_mobile)
        self.assertFalse(form.is_valid())
        self.assertRaises(ValueError, form.save)
        self.assertEqual(
            form.errors.get("model")[0],
            "Mobile with this Model already exists.",
        )
