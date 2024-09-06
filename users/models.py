from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models

from habit.models import NULLABLE


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError
        if extra_fields.get("is_superuser") is not True:
            raise ValueError

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    objects = UserManager()

    username = None
    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите свою почту"
    )
    phone = models.CharField(
        max_length=35, **NULLABLE, verbose_name="Телефон", help_text="Укажите  номер телефона"
    )
    city = models.CharField(
        max_length=150,
        **NULLABLE,
        verbose_name="Город",
        help_text="Укажите город",
    )

    tg_nick = models.CharField(
        max_length=50,
        **NULLABLE,
        verbose_name="Tg name",
        help_text="Укажите telegram-ник",
    )

    tg_chat_id = models.CharField(
        max_length=50,
        verbose_name="Телеграм chat-id",
        help_text="Укажите телеграм chat-id",
    )
    time_offset = models.IntegerField(
        default=3,
        verbose_name="Смещение часового пояса",
        help_text="От -12 до +14, по умолчанию UTC+3 (Московское время)"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return f"{self.email}"
