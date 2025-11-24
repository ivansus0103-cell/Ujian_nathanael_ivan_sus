from django.shortcuts import render, get_object_or_404, redirect
from .models import Gudang, Produk, Pembelian, Pesanan
from .forms import GudangForm, PembelianForm, PesananForm

def index(request):
    return render(request, 'inventory/index.html', {
        'gudangs': Gudang.objects.all(),
        'produks': Produk.objects.all(),
    })

def gudang_detail(request, pk):
    g = get_object_or_404(Gudang, pk=pk)
    return render(request, 'inventory/gudang_detail.html', {'gudang': g})

def gudang_list(request):
    data = Gudang.objects.all()
    return render(request, "inventory/gudang_list.html", {"data": data})

def pembelian_list(request):
    data = Pembelian.objects.all()
    return render(request, "inventory/pembelian_list.html", {"data": data})

def pesanan_list(request):
    data = Pesanan.objects.all()
    return render(request, "inventory/pesanan_list.html", {"data": data})

def gudang_create(request):
    form = GudangForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("inventory:gudang_list")
    return render(request, "inventory/gudang_form.html", {"form": form})

def gudang_update(request, id):
    obj = get_object_or_404(Gudang, id=id)
    form = GudangForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("inventory:gudang_list")
    return render(request, "inventory/gudang_form.html", {"form": form})

def gudang_delete(request, id):
    obj = get_object_or_404(Gudang, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("inventory:gudang_list")
    return render(request, "inventory/gudang_confirm_delete.html", {"obj": obj})

def pembelian_list(request):
    data = Pembelian.objects.all()
    return render(request, "inventory/pembelian_list.html", {"data": data})

def pembelian_create(request):
    form = PembelianForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("inventory:pembelian_list")
    return render(request, "inventory/pembelian_form.html", {"form": form})

def pembelian_update(request, id):
    obj = get_object_or_404(Pembelian, id=id)
    form = PembelianForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("inventory:pembelian_list")
    return render(request, "inventory/pembelian_form.html", {"form": form})

def pembelian_delete(request, id):
    obj = get_object_or_404(Pembelian, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("inventory:pembelian_list")
    return render(request, "inventory/pembelian_confirm_delete.html", {"obj": obj})

def pesanan_list(request):
    data = Pesanan.objects.all()
    return render(request, "inventory/pesanan_list.html", {"data": data})

def pesanan_create(request):
    form = PesananForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("inventory:pesanan_list")
    return render(request, "inventory/pesanan_form.html", {"form": form})

def pesanan_update(request, id):
    obj = get_object_or_404(Pesanan, id=id)
    form = PesananForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("inventory:pesanan_list")
    return render(request, "inventory/pesanan_form.html", {"form": form})

def pesanan_delete(request, id):
    obj = get_object_or_404(Pesanan, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("inventory:pesanan_list")
    return render(request, "inventory/pesanan_confirm_delete.html", {"obj": obj})