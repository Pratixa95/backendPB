# from rest_framework import serializers
# from .models import Portfolio

# class PortfolioSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Portfolio
#         fields = '__all__'

from rest_framework import serializers
from .models import Portfolio, GalleryImage, ContactMessage

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ['id', 'image']

class PortfolioSerializer(serializers.ModelSerializer):
    gallery_images = GalleryImageSerializer(many=True, read_only=True)

    class Meta:
        model = Portfolio
        fields = '__all__'



class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = "__all__"
