
from django.shortcuts import get_object_or_404
import json
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

from django.conf import settings
from sqlalchemy import create_engine
import pandas as pd


from django.shortcuts import render

from rest_framework import viewsets

from restapi.serializers import ServicesAreaSerializer, PolygonsSerializer
from restapi.models import ServicesArea, Polygon




class ServicesAreaViewSet(APIView):

    def post(self,request):
        serializer = ServicesAreaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            service = ServicesArea.objects.get(service_id=id)
            serializer = ServicesAreaSerializer(service)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        service = ServicesArea.objects.all()
        serializer = ServicesAreaSerializer(service, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        service = ServicesArea.objects.get(service_id=id)
        serializer = ServicesAreaSerializer(service, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        service = get_object_or_404(ServicesArea, service_id=id)
        service.delete()
        return Response({"status": "success", "data": "Item Deleted"})


class PolygonsViewSet(APIView):

    def post(self,request):
        serializer = PolygonsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            polygon = Polygon.objects.filter(services=id)
            serializer = PolygonsSerializer(polygon, many= True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        polygon = Polygon.objects.all()
        serializer = PolygonsSerializer(polygon, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        polygon = Polygon.objects.filter(services=id)
        serializer = PolygonsSerializer(polygon, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        polygon = get_object_or_404(Polygon, services=id)
        polygon.delete()
        return Response({"status": "success", "data": "Item Deleted"})


#class PolygonsViewSet(viewsets.ModelViewSet):

#    queryset = Polygon.objects.all()
#    serializer_class = PolygonsSerializer
