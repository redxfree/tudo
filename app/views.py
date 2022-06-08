from .serializers import Activeserializer, Commodity, Commodityseraializer
from rest_framework import generics
from rest_framework.response import Response
from .models import Commodity,User

# Create your views here.


class CommodityCreate(generics.CreateAPIView):
    queryset = Commodity.objects.all()
    serializer_class = Commodityseraializer
    
    
class CommodityList(generics.ListAPIView):
    queryset = Commodity.objects.all()
    serializer_class = Commodityseraializer
    
class CommodityUpdate(generics.UpdateAPIView):
    queryset = Commodity.objects.all()
    serializer_class = Commodityseraializer
    

class CommodityDestroy(generics.RetrieveDestroyAPIView):
	queryset = Commodity.objects.all()
	serializer_class = Commodityseraializer

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)

class Active(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = Activeserializer
    
    