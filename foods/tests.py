from django.test import TestCase
from rest_framework import status

from .models import Food,FoodCategory


class FoodTestCase(TestCase):
    def setUp(self):
        FoodCategory.objects.create(name_ru="Напитки")
        FoodCategory.objects.create(name_ru="Выпечка")

        Food.objects.create(
            category_id=1,
            name_ru="Чай",
            code=1,
            internal_code=100,
            cost=123.00,
            is_publish=True,
        )

        Food.objects.create(
            category_id=1,
            name_ru="Кола",
            code=2,
            internal_code=200,
            cost=123.00,
            is_publish=True,
        )

        Food.objects.create(
            category_id=1,
            name_ru="Спрайт",
            code=3,
            internal_code=300,
            cost=123.00,
            is_publish=True,
        )

        Food.objects.create(
            category_id=1,
            name_ru="Байкал",
            code=4,
            internal_code=400,
            cost=123.00,
            is_publish=True,
        )

        Food.objects.create(
            category_id=2,
            name_ru="Сдобная",
            code=5,
            internal_code=500,
            cost=90.00,
            is_publish=False,
        )

    def test_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_food_category(self):
        response = self.client.get("/api/v1/foods/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(len(response.data[0]["foods"]), 1)
