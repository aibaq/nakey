from django.utils.decorators import method_decorator
from nakey.utils.decorators import response_wrapper
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import *
import logging

logger = logging.getLogger(__name__)


@method_decorator(response_wrapper(), name='dispatch')
class BannerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Banner.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = BannerSerializer


@method_decorator(response_wrapper(), name='dispatch')
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CategorySerializer


@method_decorator(response_wrapper(), name='dispatch')
class ColorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Color.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ColorSerializer


@method_decorator(response_wrapper(), name='dispatch')
class SizeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Size.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SizeSerializer


@method_decorator(response_wrapper(), name='dispatch')
class ManufactureViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Manufacture.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ManufactureSerializer


@method_decorator(response_wrapper(), name='dispatch')
class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ItemSerializer


@method_decorator(response_wrapper(), name='dispatch')
class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ('post',)
    serializer_class = RequestCreateSerializer
