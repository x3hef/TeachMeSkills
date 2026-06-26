from django.db import models
from django.urls import reverse


# модели это связующее звено между нашим проектом и базами данными
# Это связующее звено позволяющее сформировать базу данных под нужды проекта
# тут прописывают все что нужно для базы данных.

# Первоначальная можель
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)  # db_index=True создать индекс для данного поля.
    slug = models.SlugField(max_length=100, unique=True)  # unique=True - делает уникальным значение.

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',
                                 on_delete=models.CASCADE)
    # ForeignKey - что в ячейку категория засунули модель. Наследование.
    # related_name='products' - Отображение имени в админке
    # on_delete=models.CASCADE - Параметр если мы удалим категорию появится окошко предупреждения.
    # on_delete=models.PROTECT - она не даст удалить категорию пока там есть хоть какие данные.
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    # blank=True - Означает что поле в админке может быть пустое.
    # 'products/%Y/%m/%d' - путь по которому будет, хранится фотография
    description = models.TextField(blank=True)  # - описание товара
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product_detail', args=[self.id, self.slug])

# python manage.py makemigrations
# (Django_kurs) PS C:\Users\xthef\PycharmProjects\TeachMeSkills\Django_kurs\shop> python manage.py makemigrations
# Migrations for 'main':
#   main\migrations\0001_initial.py
#     + Create model Category
#     + Create model Product


