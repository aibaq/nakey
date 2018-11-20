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
urlpatterns = router.urls
