from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserLimitedSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "tg_nick", "tg_nick", "tg_chat_id", "last_login",
                  "avatar", "date_joined", "is_superuser", "is_staff", "is_active", "time_offset")
