from django.db import models
from nakey.mixins.models import TimestampMixin
from nakey.utils.upload import banner_upload, item_upload


class Banner(TimestampMixin, models.Model):
    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннера'
    name = models.CharField(max_length=500, verbose_name='Наименование')
    image = models.ImageField(upload_to=banner_upload)


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    name = models.CharField(max_length=500, verbose_name='Наименование')


class Color(models.Model):
    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'
    name = models.CharField(max_length=500, verbose_name='Наименование')


class Size(models.Model):
    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'
    name = models.CharField(max_length=500, verbose_name='Наименование')


class Manufacture(models.Model):
    class Meta:
        verbose_name = 'Про'
        verbose_name_plural = 'Размеры'
    name = models.CharField(max_length=500, verbose_name='Наименование')


class Item(TimestampMixin, models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    name = models.CharField(max_length=500, verbose_name='Наименование')
    price = models.PositiveIntegerField(verbose_name='Цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    colors = models.ManyToManyField(Color)
    sizes = models.ManyToManyField(Size)
    manufacture = models.ForeignKey(Manufacture, on_delete=models.DO_NOTHING)
    description = models.TextField(verbose_name='Описание')
    # TODO: состав


class ItemImage(models.Model):
    class Meta:
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фотки товара'
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=item_upload)


class Request(TimestampMixin, models.Model):
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
    full_name = models.CharField(max_length=200, blank=True, verbose_name='ФИО')
    phone = models.CharField(max_length=100, blank=True, verbose_name='Телефон')
    address = models.CharField(max_length=1000, blank=True, verbose_name='Адрес')
    email = models.EmailField(max_length=1000, blank=True, verbose_name='Email')


class RequestItem(TimestampMixin, models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    count = models.PositiveIntegerField(default=1, verbose_name='Кол-во')
