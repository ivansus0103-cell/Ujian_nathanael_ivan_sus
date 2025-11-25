from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Gudang, Pembelian, Pesanan
from .serializers import GudangSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def api_gudang_list(request , id=None):

    # GET list
    if request.method == 'GET':
        gudang = Gudang.objects.all()
        serializer = GudangSerializer(gudang, many=True)
        return Response(serializer.data)

    # POST create
    elif request.method == 'POST':
        serializer = GudangSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    # PUT update
    elif request.method == 'PUT':
        try:
            gudang = Gudang.objects.get(id=request.data.get("id"))
        except Gudang.DoesNotExist:
            return Response({"detail": "Not found"}, status=404)

        serializer = GudangSerializer(gudang, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # DELETE
    elif request.method == 'DELETE':
        try:
            gudang = Gudang.objects.get(id=request.data.get("id"))
        except Gudang.DoesNotExist:
            return Response({"detail": "Not found"}, status=404)

        gudang.delete()
        return Response({"detail": "Deleted"}, status=204)


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def api_pembelian_list(request, id=None):
     # GET → ambil semua data
    if request.method == 'GET':
        pembelian = Pembelian.objects.all()
        serializer = PembelianSerializer(pembelian, many=True)
        return Response(serializer.data)

    # POST → tambah data
    elif request.method == 'POST':
        serializer = PembelianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    # PUT → update data (butuh ID)
    elif request.method == 'PUT':
        try:
            pembelian = Pembelian.objects.get(id=request.data.get("id"))
        except Pembelian.DoesNotExist:
            return Response({"detail": "Not found"}, status=404)

        serializer = PembelianSerializer(pembelian, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # DELETE → hapus data (butuh ID)
    elif request.method == 'DELETE':
        try:
            pembelian = Pembelian.objects.get(id=request.data.get("id"))
        except Pembelian.DoesNotExist:
            return Response({"detail": "Not found"}, status=404)

        pembelian.delete()
        return Response({"detail": "Deleted"}, status=204)

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def api_pesanan_list(request, id=None):
     # GET → ambil semua data
    if request.method == 'GET':
        pesanan = Pesanan.objects.all()
        serializer = PesananSerializer(pesanan, many=True)
        return Response(serializer.data)

    # POST → tambah data
    elif request.method == 'POST':
        serializer = PesananSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    # PUT → update data (butuh ID)
    elif request.method == 'PUT':
        try:
            pesanan = Pesanan.objects.get(id=request.data.get("id"))
        except Pesanan.DoesNotExist:
            return Response({"detail": "Not found"}, status=404)

        serializer = GudangSerializer(pesanan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # DELETE → hapus data (butuh ID)
    elif request.method == 'DELETE':
        try:
            pesanan = Pesanan.objects.get(id=request.data.get("id"))
        except Pesanan.DoesNotExist:
            return Response({"detail": "Not found"}, status=404)

        pesanan.delete()
        return Response({"detail": "Deleted"}, status=204)
