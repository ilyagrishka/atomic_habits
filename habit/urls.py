from django.urls import path

from habit.apps import HabitConfig
from habit.views import HabitsListAPIView, HabitRetrieveAPIView, HabitsCreateAPIView, HabitsUpdateAPIView, \
    HabitsDestroyAPIView, HabitsPublicListAPIView

app_name = HabitConfig.name

urlpatterns = [
    path("list/", HabitsListAPIView.as_view(), name="habits_list"),
    path("<int:pk>/", HabitRetrieveAPIView.as_view(), name="habits_retrieve"),
    path("create/", HabitsCreateAPIView.as_view(), name="habits_create"),
    path("<int:pk>/update/", HabitsUpdateAPIView.as_view(), name="habits_update"),
    path("<int:pk>/delete/", HabitsDestroyAPIView.as_view(), name="habits_delete"),
    path("public/", HabitsPublicListAPIView.as_view(), name="public_list"),
]