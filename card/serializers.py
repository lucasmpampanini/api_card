from card.models import Card
from rest_framework import serializers

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class CardResponse200(serializers.Serializer):
    status = serializers.CharField(max_length=3, default='ok')

class CardValidationResponse200(serializers.Serializer):
    uuid = serializers.CharField(max_length=36)

class CardRequestBody(serializers.Serializer):
    card_number = serializers.CharField(max_length=16)