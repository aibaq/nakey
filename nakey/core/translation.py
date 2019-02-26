from modeltranslation.translator import register, TranslationOptions
from .models import Banner, Category, Color, Size, Manufacture, Item


@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'image_title')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Color)
class ColorTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Size)
class SizeTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Manufacture)
class ManufactureTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Item)
class ItemTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

