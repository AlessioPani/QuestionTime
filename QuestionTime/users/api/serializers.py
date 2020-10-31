from django.db.models import fields
from rest_framework import serializers
from users.models import CustomUser


class UserDisplaySerializer(serializers.ModelSerializer):
    '''
    Serializer that returns the username in JSON format
    of the current authenticated user.
    '''
    class Meta:
        model = CustomUser
        fields = ["username"]
