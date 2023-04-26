from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

class CombinedSerializerView(APIView):
    def get(self, request):
        serializer1 = BitCoinSerializer(data=request.data)
        serializer1.is_valid(raise_exception=True)

        serializer2 = EthereumSerializer(data=request.data)
        serializer2.is_valid(raise_exception=True)

        serializer3 = EthereumClassicSerializer(data=request.data)
        serializer3.is_valid(raise_exception=True)

        serializer4 = XRPSerializer(data=request.data)
        serializer4.is_valid(raise_exception=True)

        serializer5 = CardanoADASerializer(data=request.data)
        serializer5.is_valid(raise_exception=True)

        combined_data = {
            'data1': serializer1.validated_data,
            'data2': serializer2.validated_data,
            'data3': serializer3.validated_data,
            'data4': serializer4.validated_data,
            'data5': serializer5.validated_data,
        }

        return Response(combined_data)