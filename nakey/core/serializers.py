from rest_framework import serializers
from .models import *


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class ManufactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacture
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
    category = CategorySerializer()
    colors = ColorSerializer(many=True)
    sizes = SizeSerializer(many=True)
    manufacture = ManufactureSerializer()

    def to_representation(self, instance):
        representation = super(ItemSerializer, self).to_representation(instance)
        representation['images'] = [x.image.url for x in instance.images.all()]
        return representation


class RequestItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestItem
        fields = ('item', 'count')


class RequestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('full_name', 'phone', 'address', 'email', 'items')
    items = RequestItemCreateSerializer(many=True, help_text='''{"item": 1, "count": 10}''')

    def create(self, validated_data):
        items = validated_data.pop('items')
        instance = Request(**validated_data)
        instance.save()
        for i in items:
            RequestItem.objects.create(request=instance,
                                       item=i['item'],
                                       count=i['count'])
        instance.send_email()
        return instance
