from django.db import models
from django.utils import timezone
from django.db import transaction

class Gudang(models.Model):
    name = models.CharField(max_length=100)
    alamat = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Produk(models.Model):
    sku = models.CharField(max_length=50, unique=True)
    nama = models.CharField(max_length=200)
    deskripsi = models.TextField(blank=True)
    harga_beli = models.DecimalField(max_digits=12, decimal_places=2, default=0)  # referensi
    harga_jual = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.nama} ({self.sku})"

class GudangProduk(models.Model):
    gudang = models.ForeignKey(Gudang, on_delete=models.CASCADE, related_name="stok")
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE, related_name="stok_per_gudang")
    kuantitas = models.IntegerField(default=0)

    class Meta:
        unique_together = ('gudang', 'produk')

    def __str__(self):
        return f"{self.produk.nama} @ {self.gudang.name}: {self.kuantitas}"

    def tambah(self, qty):
        self.kuantitas += qty
        self.save()

    def kurang(self, qty):
        self.kuantitas -= qty
        if self.kuantitas < 0:
            self.kuantitas = 0  # atau raise error
        self.save()

# Pembelian (mencatat masuk barang ke gudang)

class Pembelian(models.Model):
    nomor = models.CharField(max_length=50, unique=True)
    tanggal = models.DateField(default=timezone.now)
    gudang = models.ForeignKey(Gudang, on_delete=models.PROTECT)
    total = models.DecimalField(max_digits=14, decimal_places=2, default=0)

    def proses_pembelian(self):
        from .models import GudangProduk  # import di dalam fungsi
        
        with transaction.atomic():
            for item in self.items.all():
                stok, created = GudangProduk.objects.get_or_create(
                    gudang=self.gudang,
                    produk=item.produk,
                    defaults={'kuantitas': 0}
                )
                stok.tambah(item.kuantitas)

class PurchaseItem(models.Model):
    pembelian = models.ForeignKey(Pembelian, on_delete=models.CASCADE, related_name='items')
    produk = models.ForeignKey(Produk, on_delete=models.PROTECT)
    kuantitas = models.IntegerField()
    harga_satuan = models.DecimalField(max_digits=12, decimal_places=2)

    def subtotal(self):
        return self.kuantitas * self.harga_satuan

    def __str__(self):
        return f"{self.kuantitas} x {self.produk.nama}"

# Pesanan (order pelanggan) - mengurangi stok
class Pesanan(models.Model):
    nomor = models.CharField(max_length=50, unique=True)
    tanggal = models.DateField(default=timezone.now)
    gudang = models.ForeignKey(Gudang, on_delete=models.PROTECT)
    total = models.DecimalField(max_digits=14, decimal_places=2, default=0)

    STATUS_CHOICES = [
        ('pending','Pending'),
        ('paid','Paid'),
        ('shipped','Shipped'),
        ('cancelled','Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    keterangan = models.TextField(blank=True)

    def __str__(self):
        return f"Pesanan {self.nomor}"


class OrderItem(models.Model):
    pesanan = models.ForeignKey(Pesanan, on_delete=models.CASCADE, related_name='items')
    produk = models.ForeignKey(Produk, on_delete=models.PROTECT)
    kuantitas = models.IntegerField()
    harga_satuan = models.DecimalField(max_digits=12, decimal_places=2)

    def subtotal(self):
        return self.kuantitas * self.harga_satuan

    def __str__(self):
        return f"{self.kuantitas} x {self.produk.nama}"
