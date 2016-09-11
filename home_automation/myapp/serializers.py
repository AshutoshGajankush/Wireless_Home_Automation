# Serializers for room and door REST services - serializers.py

from myapp.models import Light
from rest_framework import serializers
"""
class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('url', 'name')
"""
class LightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Light
        fields = ('url', 'name')
