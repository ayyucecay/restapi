from django.contrib import admin

from django.urls import path, include, re_path

from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("restapi.urls")),
]
