from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from fcm_django.models import FCMDevice

users = User.objects.all()
for user in users:
    fcm_devices = FCMDevice.objects.filter(user=user)
    fcm_devices.send_message(
        title="Daily dish", body="Don't forget to choose your dish for today", time_to_live=604800,
        click_action="http://localhost:8080/")
