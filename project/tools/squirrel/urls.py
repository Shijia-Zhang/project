from django.urls import path
from . import views

urlpatterns = [
        path('', views.index),
        path('sightings/', views.all_squirrels),
        path('sightings/add/', views.add_squirrel,name='add'),
        path('sightings/<unique_squirrel_ID>/', views.update_squirrel,name='update'),
        path('map/', views.map,name='map'),
  ]
