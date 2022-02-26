from django.urls import path
from . import views


urlpatterns = [
    path('services', views.ServicesAreaViewSet.as_view()),
    path('services/<int:id>',views.ServicesAreaViewSet.as_view()),
    path('services/<int:id>/change', views.ServicesAreaViewSet.as_view()),
    path('polygons', views.PolygonsViewSet.as_view()),
    path('polygons/<int:id>', views.PolygonsViewSet.as_view()),

    # for testing
    #path('test/', views.test_view, name="test_view")
]
