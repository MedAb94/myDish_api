from rest_framework import routers
from django.urls import path, include
from .api import (dishes_api, )

urlpatterns = [
    path('', dishes_api, name='allDishes'),

]
