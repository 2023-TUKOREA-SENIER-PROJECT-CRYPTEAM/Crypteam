from .models import *
from rest_framework import serializers

class BitCoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitCoin
        fields = '__all__'

class EthereumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ethereum
        fields = '__all__'

class EthereumClassicSerializer(serializers.ModelSerializer):
    class Meta:
        model = EthereumClassic
        fields = '__all__'

class XRPSerializer(serializers.ModelSerializer):
    class Meta:
        model = XRP
        fields = '__all__'

class CardanoADASerializer(serializers.ModelSerializer):
    class Meta:
        model = CardanoADA
        fields = '__all__'
