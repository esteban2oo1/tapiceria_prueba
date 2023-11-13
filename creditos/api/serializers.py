from rest_framework import serializers
from creditos.models import Creditos

class CreditosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creditos
        fields = '__all__'
