from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=240)
    email = serializers.EmailField()
    wishlist = serializers.ForeignKey()
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