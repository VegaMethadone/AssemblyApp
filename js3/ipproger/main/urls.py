
from django.urls import path
from .  import views

#urlpatterns = [
#    path('', views.index, name='pie-chart'),
#]



urlpatterns = [
    path('', views.index, name='index'),
    path('json/', views.json, name='json')
]

# path('разобр', views.index, name='pie-chart'),

