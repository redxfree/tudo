from logging import raiseExceptions
from pickle import TRUE
from .serializers import Activeserializer, Commodity, Commodityseraializer
from rest_framework import generics
from rest_framework.response import Response
from .models import Commodity,User
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class CommodityCreate(generics.CreateAPIView):
	queryset = Commodity.objects.all()
	serializer_class = Commodityseraializer

	def post(self,request,*args,**kwargs):
		serializer = self.get_serializer(data = request.data)
		serializer.is_valid(raise_exception = TRUE)
		commodity  = serializer.save()
	
		return Response({
			"commodity" : Commodityseraializer(commodity,context = self.get_serializer_context()).data,
			"message" : "created "
		})
    
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



