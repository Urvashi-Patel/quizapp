from rest_framework import serializers
from .models import User

class Serializationclass(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'