from django.views import View
from django.shortcuts import get_object_or_404, render
from nakey.core.serializers import *
from nakey.utils import constants


class IndexView(View):
    template_name = 'core/index.html'

    def get(self, request):
        context = {'banners': Banner.objects.all(),
                   'popular_items': Item.objects.all().order_by('-view_count')[:constants.POPULAR_COUNT]}
        return render(request, self.template_name, context)


class ShopView(View):
    template_name = 'core/shop.html'
    queryset = Item.objects.all()

    def get(self, request, *args, **kwargs):
        context = {'categories': Category.objects.all()}
        return render(request, self.template_name, context)


class ItemView(View):
    template_name = 'core/item.html'

    def get(self, request, pk, *args, **kwargs):
        item = get_object_or_404(Item, pk=pk)
        return render(request, self.template_name, {'item': item})


class ContactsView(View):
    template_name = 'core/contacts.html'

    def get(self, request, pk, *args, **kwargs):
        return render(request, self.template_name)
