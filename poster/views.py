from django.shortcuts import render
from rest_framework.response import Response
from .models import Poster
from rest_framework.views import APIView
from rest_framework import status
from .serializers import PosterCreateSerializer,PosterSerializer


# Create your views here.


class PosterView(APIView):
    def post(self, request, format=None):
        if request.user.is_superuser:
            data= request.data
            serializer= PosterCreateSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Permission error":"Only Superuser allowed to access"})
            
    def put(self, request, pk, format=None):
        if request.user.is_superuser:
            data=request.data
            mov = Poster.objects.get(id=pk)
            serializer = PosterCreateSerializer(data=data, instance=mov)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Permission error":"Only Superuser allowed to access"})

    def get(self,request, pk=None, format=None):
        if request.user.is_superuser:

            if pk:
                mov = Poster.objects.get(pk=pk)
                serializer = PosterSerializer(mov)

            else:
                mov=Poster.objects.all()
                serializer = PosterSerializer(mov, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"Permission error":"Only Superuser allowed to access"})

    def delete(self, request, pk, format=None):
        if request.user.is_superuser:
            mov = Poster.objects.get(pk=pk)
            mov.delete()
            return Response({"msg":"Data Deleted!!!!!"}, status=status.HTTP_200_OK)
        else:
            return Response({"Permission error":"Only Superuser allowed to access"})
