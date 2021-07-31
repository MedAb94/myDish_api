from django.urls import path, include
from .api import (login, get_choices, create_choice, get_user_choices, get_day_order)
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet

urlpatterns = [
    path('', get_choices, name='allChoices'),
    path('get-order', get_day_order, name='DayOrder'),
    path('user-choices/<user_id>', get_user_choices, name='userChoices'),
    path('login', login, name='Login'),
    path('create-choice/<uid>/<did>', create_choice, name='createChoice'),
    path('register-notif-token/',
         FCMDeviceAuthorizedViewSet.as_view({'post': 'create'}), name='create_fcm_device'),
]
