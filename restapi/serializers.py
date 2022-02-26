from rest_framework import serializers

from restapi.models import ServicesArea,Polygon

class ServicesAreaSerializer(serializers.ModelSerializer):
   class Meta:
       model = ServicesArea
       fields = ('service_id', 'name', 'email', 'phone_number', 'language', 'currency')

class PolygonsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Polygon
       fields = ('name', 'price', 'geojson',  'services')
