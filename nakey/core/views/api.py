from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from nakey.core.serializers import *
from nakey.utils.decorators import response_wrapper
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
import logging

logger = logging.getLogger(__name__)


@method_decorator(response_wrapper(), name='dispatch')
class BannerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


@method_decorator(response_wrapper(), name='dispatch')
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@method_decorator(response_wrapper(), name='dispatch')
class ColorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


@method_decorator(response_wrapper(), name='dispatch')
class SizeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


@method_decorator(response_wrapper(), name='dispatch')
class ManufactureViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Manufacture.objects.all()
    serializer_class = ManufactureSerializer


@method_decorator(response_wrapper(), name='dispatch')
class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_fields = ('category', 'manufacture')
    search_fields = ('name',)
    ordering_fields = ('view_count', 'price')


@method_decorator(response_wrapper(), name='dispatch')
class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    http_method_names = ('post',)
    serializer_class = RequestCreateSerializer
