from rest_framework import serializers
from .models import (User, Sub)

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=240)
    email = serializers.EmailField()
    wishlist = serializers.RelatedField(source = 'Post', read_only = True)
    registationDate = serializers.DateField()

    def create(self, validated_data):
        return User.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.wishlist = validated_data.get('wishlist', instance.wishlist)
        instance.registrationDate = validated_data.get('registrationDate', instance.registrationDate)
        instance.save()
        return instance

class SubSerializer(serializers.Serializer):
    class Meta:
        model = Sub
        fields = ['id', 'name', 'brand', 'size', 'rms', 'peak']
    # name = serializers.CharField(max_length=240)
    # brand = serializers.CharField(max_length=240)
    # size = serializers.CharField(max_length=240)
    # rms = serializers.CharField(max_length=240)
    # peak = serializers.CharField(max_length=240)

    # def create(self, validated_data):
    #     return Sub.objects.create(validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.brand = validated_data.get('brand', instance.brand)
    #     instance.size = validated_data.get('size', instance.size)
    #     instance.rms = validated_data.get('rms', instance.rms)
    #     instance.peak = validated_data.get('peak', instance.peak)
    #     instance.save()
    #     return instance