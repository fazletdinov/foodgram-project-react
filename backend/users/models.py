from django.contrib.auth.models import AbstractUser
from django.db import models
from foodgram.settings import MAX_LENGTH_150, MAX_LENGTH_254
from users.validators import validate_username


class CustomUser(AbstractUser):
    """Пользовательская модель пользователя"""
    email = models.EmailField(
        'Электронная почта',
        max_length=MAX_LENGTH_254,
        unique=True,
        blank=False,
        null=False,
    )
    username = models.CharField(
        'Имя пользователя',
        max_length=MAX_LENGTH_150,
        unique=True,
        blank=False,
        null=False,
        validators=[validate_username, ]
    )
    first_name = models.CharField(
        'Имя',
        max_length=MAX_LENGTH_150,
        blank=False,
        null=False,
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=MAX_LENGTH_150,
        blank=False,
        null=False
    )
    password = models.CharField(
        'Пароль',
        max_length=MAX_LENGTH_150,
        blank=False,
        null=False,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Subscription(models.Model):
    """Модель для подписок"""
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Пользователь',
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='unique_user_author'
            ),
            models.CheckConstraint(
                check=~models.Q(author=models.F("user")),
                name="Нельзя подписываться на самого себя"
            )
        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'{self.user.username} подписан на {self.author.username}'
