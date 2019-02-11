from django.conf import settings
from django.template.loader import render_to_string
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from nakey.core import tasks
from nakey.mixins.models import TimestampMixin
from nakey.utils import constants, messages
from nakey.utils.upload import banner_upload, item_upload


class Banner(TimestampMixin, models.Model):
    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннера'
    title = models.CharField(max_length=500, verbose_name='Наименование')
    subtitle = models.CharField(max_length=500, verbose_name='Наименование 2')
    image = models.ImageField(upload_to=banner_upload)
    image_title = models.CharField(max_length=500, verbose_name='Наименование ссылки')

    def __str__(self):
        return self.title


class Category(MPTTModel):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    name = models.CharField(max_length=500, verbose_name='Наименование')
    parent = TreeForeignKey('self', null=True, blank=True, on_delete=models.CASCADE,
                            related_name='children', db_index=True)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Color(models.Model):
    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'
    name = models.CharField(max_length=500, verbose_name='Наименование')

    def __str__(self):
        return self.name


class Size(models.Model):
    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'
    name = models.CharField(max_length=500, verbose_name='Наименование')

    def __str__(self):
        return self.name


class Manufacture(models.Model):
    class Meta:
        verbose_name = 'Про'
        verbose_name_plural = 'Размеры'
    name = models.CharField(max_length=500, verbose_name='Наименование')

    def __str__(self):
        return self.name


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
    view_count = models.PositiveIntegerField(default=10, verbose_name='Просмотры')
    # TODO: состав


class ItemImage(models.Model):
    class Meta:
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фотки товара'
        ordering = ('priority',)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=item_upload)
    priority = models.PositiveIntegerField(default=1, db_index=True)


class Request(TimestampMixin, models.Model):
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
    full_name = models.CharField(max_length=200, blank=True, verbose_name='ФИО')
    phone = models.CharField(max_length=100, blank=True, verbose_name='Телефон')
    address = models.CharField(max_length=1000, blank=True, verbose_name='Адрес')
    email = models.EmailField(max_length=1000, blank=True, verbose_name='Email')

    def send_email(self):
        message = render_to_string('emails/request.html', {'req': self,
                                                           'request_items': self.items.all()})
        if settings.CELERY_ON:
            tasks.email(to=constants.RECEIVER_EMAIL, subject=messages.REQUEST_SUBJECT, message=message)


class RequestItem(TimestampMixin, models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    count = models.PositiveIntegerField(default=1, verbose_name='Кол-во')
