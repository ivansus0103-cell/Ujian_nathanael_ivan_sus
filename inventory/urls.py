from django.urls import path
from . import views, api

app_name = 'inventory'

urlpatterns = [
    path('', views.index, name='index'),
    path('gudang/<int:pk>/', views.gudang_detail, name='gudang_detail'),
    #Gudang CRUD
    path('gudang/', views.gudang_list, name="gudang_list"),
    path('gudang/create/', views.gudang_create, name="gudang_create"),
    path('gudang/update/<int:id>/', views.gudang_update, name="gudang_update"),
    path('gudang/delete/<int:id>/', views.gudang_delete, name="gudang_delete"),

    # Pembelian CRUD
    path('pembelian/', views.pembelian_list, name="pembelian_list"),
    path('pembelian/create/', views.pembelian_create, name="pembelian_create"),
    path('pembelian/update/<int:id>/', views.pembelian_update, name="pembelian_update"),
    path('pembelian/delete/<int:id>/', views.pembelian_delete, name="pembelian_delete"),

    # Pesanan CRUD
    path('pesanan/', views.pesanan_list, name="pesanan_list"),
    path('pesanan/create/', views.pesanan_create, name="pesanan_create"),
    path('pesanan/update/<int:id>/', views.pesanan_update, name="pesanan_update"),
    path('pesanan/delete/<int:id>/', views.pesanan_delete, name="pesanan_delete"),

    # API
    path('api/gudang/', api.api_gudang_list),
]
