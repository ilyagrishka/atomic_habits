from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from habit.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="ilya@test.com",
            password="password",
            tg_chat_id="11111111"
        )
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            owner=self.user,
            place="МегаМол",
            time="14:00:00",
            action="купить в моле что нибудь вкусное",
            periodicity=2,
            duration=14
        )

        self.habit_nice_false = Habit.objects.create(
            owner=self.user,
            place="дом",
            time="18:00:00",
            action="Убраться в квартире",
            is_nice=False,
            related=self.habit,
            periodicity=1,
            duration=60,
            is_public=False
        )

    def test_create_habit(self):
        url = reverse("habit:habits_create")
        data = {
            "owner": self.user.pk,
            "place": "парк",
            "time": "18:00:00",
            "action": "Пойти в парк бегать",
            "duration": 60,
            "periodicity": 1,
            "sunday": True,
            "monday": True,
            "tuesday": True,
            "wednesday": True,
            "thursday": True,
            "friday": True,
            "saturday": True
        }

        response = self.client.post(url, data=data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data.get("user"), self.user.pk)
        self.assertEqual(data.get("place"), "парк")
        self.assertEqual(data.get("time"), "18:00:00")
        self.assertEqual(data.get("step"), "Пойти в парк бегать")
        self.assertEqual(data.get("time_for_doing"), 60)
        self.assertEqual(data.get("periodiccaly"), 1)
        self.assertEqual(data.get("friday"), True)

    def test_validator(self):
        url = reverse("habit:habits_create")
        data = {
            "owner": self.user.pk,
            "place": "Магазин",
            "time": "18:00:00",
            "action": "Пойти в магазин за покупками",
            "duration": 45,
            "periodicity": 5
        }

        response = self.client.post(url, data=data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_week_periodicaly_validator(self):
        url = reverse("habit:habits_create")
        data = {
            "owner": self.user.pk,
            "place": "Магазин",
            "time": "18:00:00",
            "action": "Пойти в магазин за покупками",
            "duration": 180,
            "periodicity": 8,
            "sunday": False,
            "monday": False,
            "tuesday": False,
            "wednesday": False,
            "thursday": False,
            "friday": False,
            "saturday": False
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validate_connected_or_prize(self):
        url = reverse("habit:habits_create")
        data = {
            "owner": self.user.pk,
            "place": "Магазин",
            "time": "18:00:00",
            "action": "Пойти в магазин за покупками",
            "is_nice": True,
            "duration": 60,
            "periodicity": 1,
            "prize": "съесть бургер"
        }

        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validate_connected_is_nice(self):
        url = reverse("habits:habits_create")

        data3 = {
            "owner": self.user.pk,
            "place": "Магазин",
            "time": "19:00:00",
            "action": " пойти в магаз",
            "is_nice": False,
            "related": self.habit_nice_false,
            "duration": 60,
            "periodicity": 1,
        }
        response = self.client.post(url, data=data3)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_habit(self):

        url = reverse("habits:habits_list")
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(2, data.get("count"))

    def test_retrieve_habit(self):

        url = reverse("habit:habits_retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("user"), self.habit.user.id)
        self.assertEqual(data.get("place"), self.habit.place)
        self.assertEqual(data.get("time"), self.habit.time)
        self.assertEqual(data.get("step"), self.habit.step)
        self.assertEqual(data.get("time_for_doing"), self.habit.time_for_doing)
        self.assertEqual(data.get("periodically"), self.habit.periodically)
        self.assertEqual(data.get("friday"), True)

