from rest_framework import serializers

from habit.models import Habit
from habit.validators import HabitTimeForDoingValidator, validate_connected_or_prize, validate_connected_is_nice, \
    HabitPeriodicallyValidator


class HabitSerializer(serializers.ModelSerializer):
    validators = [HabitTimeForDoingValidator(field="time_for_doing"), HabitPeriodicallyValidator(field="periodically")]

    class Meta:
        model = Habit
        fields = "__all__"

    def validate(self, data):
        message = validate_connected_or_prize(data) + validate_connected_is_nice(data)

        if message:
            raise serializers.ValidationError(message)

        return data
