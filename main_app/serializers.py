from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=240)
    email = serializers.EmailField()
    wishlist = serializers.ForeignKey()
    registationDate = serializers.DateField()