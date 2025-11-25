from django import forms
from .models import Gudang, Pembelian, Pesanan, Produk

class GudangForm(forms.ModelForm):
    class Meta:
        model = Gudang
        fields = ['name', 'alamat']


class PembelianForm(forms.ModelForm):
    class Meta:
        model = Pembelian
        fields = ['nomor', 'tanggal', 'gudang', 'total']


class PesananForm(forms.ModelForm):
    class Meta:
        model = Pesanan
        fields = ['nomor', 'tanggal', 'gudang', 'total', 'status']

# class ProdukForm(forms.ModelForm):
#     class Meta:
#         model = Pesanan
#         fields = ['sku', 'nama', 'deskripsi', 'harga_beli', 'harga_jual']