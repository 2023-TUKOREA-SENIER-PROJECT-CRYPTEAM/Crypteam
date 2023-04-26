from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
b = BitCoin.objects.all()
serializer1 = BitCoinSerializer(b, many = True)
e = Ethereum.objects.all()
serializer2 = EthereumSerializer(e, many = True)
ec = EthereumClassic.objects.all()
serializer3 = EthereumClassicSerializer(ec, many = True)
x = XRP.objects.all()
serializer4 = XRPSerializer(x, many = True)
c = CardanoADA.objects.all()
serializer5 = CardanoADASerializer(c, many = True)


news_data = {
    "bitcoinNews": serializer1.data,
    "ethereumNews": serializer2.data,
    "ethereumclasicsNews": serializer3.data,
    "xrpNews": serializer4.data,
    "cardanoadaNews": serializer5.data
}
class NewsAPIView(APIView):
    def get(self, request):
        b = BitCoin.objects.all()
        serializer1 = BitCoinSerializer(b, many = True)
        e = Ethereum.objects.all()
        serializer2 = EthereumSerializer(e, many = True)
        ec = EthereumClassic.objects.all()
        serializer3 = EthereumClassicSerializer(ec, many = True)
        x = XRP.objects.all()
        serializer4 = XRPSerializer(x, many = True)
        c = CardanoADA.objects.all()
        serializer5 = CardanoADASerializer(c, many = True)

        news_data = {
            "bitcoinNews": serializer1.data,
            "ethereumNews": serializer2.data,
            "ethereumclasicsNews": serializer3.data,
            "xrpNews": serializer4.data,
            "cardanoadaNews": serializer5.data
        }

        return Response(news_data)



# @api_view(['GET'])
# def NewsList(request):
#     news = NewsData.objects.all()

#     serializer = NewsSerialrizer(news, many = True)

#     return Response(serializer.data)