from django.db import models

from django.db import models

# from config.settings import AUTH_USER_MODEL

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    good_choice = (
        (True, "Приятная"),
        (False, "Нет"),
    )

    public_choice = (
        (True, "Публичная"),
        (False, "Нет"),
    )

    monday = models.BooleanField(default=True, verbose_name="Понедельник")
    tuesday = models.BooleanField(default=True, verbose_name="Вторник")
    wednesday = models.BooleanField(default=True, verbose_name="Среда")
    thursday = models.BooleanField(default=True, verbose_name="Четверг")
    friday = models.BooleanField(default=True, verbose_name="Пятница")
    saturday = models.BooleanField(default=True, verbose_name="Суббота")
    sunday = models.BooleanField(default=True, verbose_name="Воскресенье")

    # user = models.ForeignKey(
    #     AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="пользователь", **NULLABLE
    # )
    #
    # place = models.CharField(max_length=140, verbose_name="место")
    # time = models.TimeField(verbose_name="время, когда надо выполнить привычку")
    # step = models.CharField(
    #     max_length=140, verbose_name="действие, которое надо сделать"
    # )

    is_nice = models.BooleanField(
        default=True, verbose_name="приятная привычка", choices=good_choice
    )
    connected = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        verbose_name="связка с другой привычкой",
        **NULLABLE,
    )
    periodically = models.SmallIntegerField(
        default=1, verbose_name="Периодичность в днях"
    )
    prize = models.CharField(max_length=100, verbose_name="Вознаграждение", **NULLABLE)
    time_for_doing = models.SmallIntegerField(verbose_name="Время на выполнение (в минутах) ")
    is_public = models.BooleanField(
        default=True, verbose_name="Публичная", choices=public_choice
    )

    def __str__(self):
        return f"Я буду {self.step} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ["id"]

