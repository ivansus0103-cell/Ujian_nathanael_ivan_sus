from django.contrib import admin
from .models import Gudang, Produk, GudangProduk, Pembelian, PurchaseItem, Pesanan, OrderItem


def proses_pembelian(modeladmin, request, queryset):
    for pembelian in queryset:
        pembelian.proses_pembelian()

proses_pembelian.short_description = "Proses pembelian (update stok)"

def proses_pesanan(modeladmin, request, queryset):
    for pesanan in queryset:
        pesanan.proses_pesanan()
        
proses_pesanan.short_description = "Proses pesanan (kurangi stok)"

class PurchaseItemInline(admin.TabularInline):
    model = PurchaseItem
    extra = 1

class PembelianAdmin(admin.ModelAdmin):
    list_display = ('nomor','tanggal','gudang','total')
    inlines = [PurchaseItemInline]
    actions = [proses_pembelian]

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class PesananAdmin(admin.ModelAdmin):
    list_display = ('nomor','tanggal','gudang','status','total')
    inlines = [OrderItemInline]
    actions = [proses_pesanan]




admin.site.register(Gudang)
admin.site.register(Produk)
admin.site.register(GudangProduk)
admin.site.register(Pembelian, PembelianAdmin)
admin.site.register(Pesanan, PesananAdmin)
