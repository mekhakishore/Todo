from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from api.serializers import Registration,User,todoserializer
from Work.models import Taskmodel
from rest_framework import authentication,permissions
from rest_framework.viewsets import ViewSet,ModelViewSet




class Userregiser(APIView): 

    def post(self,request,*args,**kwargs):

        serializer=Registration(data=request.data)

        if serializer.is_valid():

            serializer.save()

        return Response(serializer.data)  


class Todoviewsetview(ViewSet):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def list(self,*args,**kwargs):

        qs=Taskmodel.objects.all()

        serializer=todoserializer(qs,many=True)

        return Response(serializer.data)
    




    def create(self,request,*args,**kwargs):


        serializer=todoserializer(data=request.data)

        if serializer.is_valid():

            serializer.save(user=request.user)

        return Response(serializer.data)      



 







    def destroy(self,request,*args,**kwargs):

        id=kwargs.get("pk") 

        qs=Taskmodel.objects.get(id=id)
        if qs.user==request.user:

            qs.delete()

            return Response({"message":"Todo object delete"}) 
        
        else:

            raise serializers.ValidationError("not allowed")
        




    def update(self,request,*args,**kwargs):

        id=kwargs.get('pk')

        qs=Taskmodel.objects.get(id=id)

        serializer=todoserializer(data=request.data,instance=qs)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)
        
        else:

            return Response(serializer.errors)
        
    def retrieve(self,request,*args,**kwargs):

        id=kwargs.get('pk')

        qs=Taskmodel.objects.get(id=id)

        serializer=todoserializer(qs)

        return Response(serializer.data)
    


class Todomodelviewset(ModelViewSet):

    queryset=Taskmodel.objects.all()

    serializer_class=todoserializer 

    authentication_classes=[authentication.TokenAuthentication]   

    permission_classes=[permissions.IsAuthenticated]


    def get_queryset(self):
        return Taskmodel.objects.filter(user=self.request.user)
    
    def create(self,serializer):
        return serializer.save(user=self.request.user)
    
    def perform_update(self, serializer):
        return super().perform_update(serializer)


    def perform_destroy(self, instance):
       instance=Taskmodel.objects.get(id=id)
       if instance.user==self.request.user:
           
           return instance.delete()
       
       else:
           print("not allowed")


   
    

    def destroy(self,request,args,*kwargs):

        id=kwargs.get("pk") 

        qs=Taskmodel.objects.get(id=id)
        if qs.user==request.user:

            qs.delete()

            return Response({"message":"Todo object delete"})    

        

    











