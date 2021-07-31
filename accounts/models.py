from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from dishes.models import Dish


class Choice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.today(), blank=True)

    def __str__(self):
        return self.user.username + "-" + self.date.strftime('%d/%m/%Y')
