from rest_framework import serializers,routers

from .models import Information

class InformationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Information
        fields="__all__"