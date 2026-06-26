from django.db import models
from django.contrib.auth.models import User  # Стандартная библиотека пользователя


class Table(models.Model):
    """МОДЕЛЬ, КОТОРАЯ ОПИСЫВАЕТ СТОЛИК"""

    number = models.PositiveIntegerField(  # Гарантирует что номер столика не будет отрицательный
        unique=True,  # Защита от совпадения
        verbose_name="Номер столика"
    )

    image = models.ImageField(
        upload_to='tables/',  # Создаём подпапку в медиа-файлах
        blank=True,  # Позволяют создавать столик и без фото
        null=True,  # Позволяют создавать столик и без фото
        verbose_name="Фото столика"
    )

    seats = models.PositiveIntegerField(  # Своего рода защита
        verbose_name="Количество мест"
    )

    class Meta:  # Для админ панели чтоб все было красиво
        verbose_name = "Столик"
        verbose_name_plural = "Столики"
        ordering = ['number']  # Cортировать по номеру столика

    def __str__(self):
        return f"Стол под номером {self.number} ({self.seats} мест)"


class Reservation(models.Model):
    """МОДЕЛЬ ДАННЫХ О РЕЗЕРВАЦИИ СТОЛИКА"""

    table = models.ForeignKey( # Это связь, что один столик одна бронь
        Table,
        on_delete=models.CASCADE, # При удалении столика все брони тоже удаляться
        related_name='reservations', # Ключ поиска простыми словами
        verbose_name = 'Столик'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='my_bookings',
        verbose_name="Клиент"
    )

    date = models.DateField(verbose_name='Дата бронирования')
    hour_start = models.PositiveIntegerField(verbose_name="Час начала(8-18)")
    hour_end = models.PositiveIntegerField(verbose_name="Час окончания(8-18)")
    # auto_now_add=True - сам записывает время, когда пользователь нажал кнопку "Забронировать"
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи")

    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирование"
        ordering = ['-date', '-hour_start'] # Сортируем по свежей дате

    def __str__(self):
        return f"{self.user.username} | Стол номер: {self.table.number} | {self.date}"
