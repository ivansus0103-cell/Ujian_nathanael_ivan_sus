from rest_framework import serializers
from .models import Gudang, Pembelian, Pesanan

class GudangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gudang
        fields = '__all__'

class PembelianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pembelian
        fields = '__all__'

class PesananSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesanan
        fields = '__all__'