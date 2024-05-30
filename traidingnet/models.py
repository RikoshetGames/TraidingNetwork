from django.conf import settings
from django.db import models

# Create your models here.

NULLABLE = {'blank': True, 'null': True}




class Contacts(models.Model):
    contact_email = models.EmailField(verbose_name='Электронная почта')
    state = models.CharField(max_length=100, verbose_name='Страна', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    street = models.CharField(max_length=150, verbose_name='Улица', **NULLABLE)
    building = models.CharField(max_length=100, verbose_name='Номер дома', **NULLABLE)
    create_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.contact_email

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Product(models.Model):
    product_title = models.CharField(max_length=200, verbose_name='Название продукта')
    product_model = models.CharField(max_length=100, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода', **NULLABLE)
    product_price = models.FloatField(verbose_name='Цена', **NULLABLE)
    create_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.product_title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Supplier(models.Model):

    supplier_type_list = [
        (0, "Завод"),
        (1, "Розничная сеть"),
        (2, "Индивидуальный предприниматель"),
    ]

    sup_name = models.CharField(max_length=200, verbose_name='Название')
    supplier_type = models.IntegerField(choices=supplier_type_list, verbose_name='Уровень сети', default=0)
    supply_level = models.PositiveIntegerField(verbose_name='Уровень поставки')
    contact = models.ForeignKey(Contacts, on_delete=models.CASCADE, verbose_name='Контакты')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    supplier_name = models.ForeignKey('Supplier', on_delete=models.SET_NULL, verbose_name='Поставщик', **NULLABLE)
    debt = models.FloatField(verbose_name='Задолженность', **NULLABLE)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    create_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='Пользователь')

    def __str__(self):
        return self.sup_name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ['sup_name']
