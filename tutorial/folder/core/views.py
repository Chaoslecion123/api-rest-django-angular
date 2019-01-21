from rest_framework import generics
from core.models import portafolio
from core.serializers import portafolioSerializer
# Create your views here.

class portafolioList(generics.ListCreateAPIView):
    queryset = portafolio.objects.all()
    serializer_class = portafolioSerializer

class portafolioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = portafolio.objects.all()
    serializer_class = portafolioSerializer