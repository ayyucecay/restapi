
from django.shortcuts import get_object_or_404
import json
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.db import connection
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


def test_view(request):


    query = "SELECT * FROM ServicesArea WHERE service_id = {}".format(1)
#    query = "select student_name as full_name, student_email as email from students where branch_id = 11"
    service_email = pd.read_sql(query, connection)
    service_email_result = service_email.to_dict('records')
    service_email_json = json.dumps(service_email_result)
    parse_json = json.loads(service_email_json)
    print(parse_json)


    for service in parse_json:

        service_info = {
            "name": service["name"],
            "email": service["email"],
            "phone_number": service["phonenumber"],
            "language": service["language"],
            "currency": service["currency"]
        }
        try:
            requests.post('http://localhost:8000/services', data=service_info)
            #StudentsView.post(self, student_info)
        except ApiClientError as error:
            print("Error: {}".format(error.text))

    query = "SELECT * FROM Polygon WHERE services = {}".format(1)
    polygon = pd.read_sql(query, connection)
    polygon_result = polygon.to_dict('records')
    polygon_json = json.dumps(polygon_result)
    parse_json2 = json.loads(polygon_json)
    print(parse_json2)

    for polygon in parse_json2:

        polygon_info = {
            "name": polygon["name"],
            "price": polygon["price"],
            "geojson": polygon["geojson"],
            "services": polygon["services"],
        }
        try:
            requests.post('http://localhost:8000/polygons', data=polygon_info)
            #StudentsView.post(self, student_info)
        except ApiClientError as error:
            print("Error: {}".format(error.text))
            

    data = {}
#    return Response({"status": "success", "data": serializer.data})
    return render(request, "test_view.html", data)







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
