from core.models import portafolio
from rest_framework import serializers


class portafolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = portafolio
        fields = ('id','title','description','langs')

