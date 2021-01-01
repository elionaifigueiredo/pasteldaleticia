from rest_framework import serializers
from .models import Pastel
class MyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pastel
        fields = '__all__'