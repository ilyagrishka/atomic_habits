# from rest_framework import serializers
#
#
# class HabitTimeForDoingValidator:
#     def __init__(self, field):
#         self.field = field
#
#     def __call__(self, value):
#         time_for_doing = dict(value).get(self.field)
#         if time_for_doing > 120:
#             raise serializers.ValidationError("Время выполнения должно быть не больше 120 секунд.")
#
#
# class HabitPeriodicallyValidator:
#     def __init__(self, field):
#         self.field = field
#
#     def __call__(self, value):
#         periodically = dict(value).get(self.field)
#         if 7 < periodically or periodically < 1:
#             raise serializers.ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")
#
#
# def validate_connected_or_prize(data):
#     message = "У приятной привычки не может быть вознаграждения или связанной привычки. "
#     if data.get("connected") and data.get("prize"):
#         return message
#     else:
#         return ""
#
#
# def validate_connected_is_nice(data):
#     message = "В связанные привычки могут попадать только привычки с признаком приятной привычки. "
#     if data.get("connected") and (not data.get("connected").is_nice):
#         return message
#     else:
#         return ""
#
