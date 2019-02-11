from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'banner', BannerViewSet, base_name='banner')
router.register(r'category', CategoryViewSet, base_name='category')
router.register(r'color', ColorViewSet, base_name='color')
router.register(r'size', SizeViewSet, base_name='size')
router.register(r'manufacture', ManufactureViewSet, base_name='manufacture')
router.register(r'item', ItemViewSet, base_name='item')
router.register(r'request', RequestViewSet, base_name='request')
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop/item/<int:pk>/', ItemView.as_view(), name='item'),
    path('cart/', CartView.as_view(), name='cart'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('about/', AboutView.as_view(), name='about'),
]
urlpatterns += router.urls
