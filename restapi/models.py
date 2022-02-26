from django.db import models

class ServicesArea(models.Model):
   service_id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=100)
   email = models.EmailField(max_length=254)
   phone_number = models.CharField(max_length=100)
   language = models.CharField(max_length=100)
   currency = models.CharField(max_length=100)

   def __str__(self):
        return self.name

class Polygon(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    geojson = models.CharField(max_length=100)
    services = models.ForeignKey(ServicesArea, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name
