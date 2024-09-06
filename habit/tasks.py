from datetime import datetime

from django.utils import timezone
from celery import shared_task
from habit.services import send_telegram_message
from habit.models import Habit


@shared_task
def send_information_about_habit(message, tg_chat_id):
    send_telegram_message(message, tg_chat_id)


@shared_task
def find_all_habits():
    habit_time = datetime.now().replace(second=0, microsecond=0)

    habit_weekday = timezone.now().today().weekday()

    habits = Habit.objects.filter(owner__isnull=False, utc_time=habit_time)

    for habit in habits:
        habit_weekday += habit.weekday_offset
        if habit_weekday > 6:
            habit_weekday -= 7
        elif habit_weekday < 0:
            habit_weekday += 7

        tg_chat_id = habit.user.tg_chat_id
        message = f"Я буду (действие): [{habit.step}] в (место): [{habit.place}] (время): [{habit.time}]"

        if habit_weekday == 0:
            if habit.monday:
                send_information_about_habit.delay(tg_chat_id, message)
        elif habit_weekday == 1:
            if habit.tuesday:
                send_information_about_habit.delay(tg_chat_id, message)
        elif habit_weekday == 2:
            if habit.wednesday:
                send_information_about_habit.delay(tg_chat_id, message)
        elif habit_weekday == 3:
            if habit.thursday:
                send_information_about_habit.delay(tg_chat_id, message)
        elif habit_weekday == 4:
            if habit.friday:
                send_information_about_habit.delay(tg_chat_id, message)
        elif habit_weekday == 5:
            if habit.saturday:
                send_information_about_habit.delay(tg_chat_id, message)
        else:
            if habit.sunday:
                send_information_about_habit.delay(tg_chat_id, message)