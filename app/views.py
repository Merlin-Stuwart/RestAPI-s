from django.shortcuts import render
from rest_framework.views import APIView
from app.models import *
from app.serializers import *
from rest_framework.response import Response
# Create your views here.

class products(APIView):
    def get(self,request,pk):
        SDO=product.objects.all()
        GSPO=productMs(SDO,many=True)
        return Response(GSPO.data)
    def post(self,request,pk):
        PPO=request.data
        MPPO=productMs(data=PPO)
        if MPPO.is_valid():
            MPPO.save()
            return Response({'success':'This data is added succesfully'})
        else:
            return Response({'failed':'your data is failed to save'})
    
    def put(self,request,pk):
        PPO=request.data
        instance=product.objects.get(pk=pk)
        PUO=productMs(instance,data=PPO)
        if PUO.is_valid():
            PUO.save()
            return Response({'Updation':'Updated successfully'})
        else:
            return Response({'Updation':'Failed to update'})
    
    def patch(self,request,pk):
        PPO=request.data
        instance=product.objects.get(pk=pk)
        PUO=productMs(instance,data=PPO,partial=True)
        if PUO.is_valid():
            PUO.save()
            return Response({'Updation':'Updated successfully'})
        else:
            return Response({'Updation':'Failed to update'})
        
    def delete(self,request,pk):
        product.objects.get(pk=pk).delete()
        return Response({'Deletion':'Successfully deleted'})
    


