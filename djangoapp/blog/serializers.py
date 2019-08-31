from rest_framework import serializers

from .models import Category, News


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

    def get_f_thumbnail(self, obj):
        if obj.f_thumbnail:
            return obj.f_thumbnail.url
