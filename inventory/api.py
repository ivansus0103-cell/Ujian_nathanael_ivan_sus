from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Gudang
from .serializers import GudangSerializer

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def api_gudang_list(request):
    gudang = Gudang.objects.all()
    serializer = GudangSerializer(gudang, many=True)
    return Response(serializer.data)
