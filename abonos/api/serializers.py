from rest_framework import serializers
from abonos.models import Abonos

class AbonosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonos
        fields = '__all__'
