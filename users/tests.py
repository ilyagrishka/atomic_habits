# from django.test import TestCase
#
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
#
# from users.models import User
#
#
# class UserTestCase(APITestCase):
#     def setUp(self):
#         self.user = User.objects.create(
#             email="ilya@test.com",
#             password="password",
#             tg_chat_id="1111111111111",
#             time_offset=5
#         )
#
#         self.client.force_authenticate(user=self.user)
#
#     def test_create_user(self):
#         url = reverse("users:register")
#         data = {
#             "email": "ilya@test.com",
#             "password": "password",
#             "tg_chat_id": "11111111111",
#             "is_superuser": "False"
#         }
#
#         response = self.client.post(url, data=data)
#         data = response.json()
#
#         print(data)
#
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(data.get("email"), "ilya@test.com")
#         self.assertEqual(data.get("password"), None)
#         self.assertEqual(data.get("tg_chat_id"), "111111111")
#         self.assertEqual(data.get("is_superuser"), False)
#
#     def test_user_retrieve(self):
#
#         url = reverse("users:users_retrieve_update", args=(self.user.pk,))
#         response = self.client.get(url)
#         data = response.json()
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(data.get("email"), "ilya@test.com")
#         self.assertEqual(data.get("password"), None)
#         self.assertEqual(data.get("tg_chat_id"), "111111111")
#         self.assertEqual(data.get("is_superuser"), False)
