from django.contrib import admin
from .models import Choice


# Register your models here.
class ChoicesAdmin(admin.ModelAdmin):
    # list_display = ('id', 'user', 'dish')

    list_per_page = 25


admin.site.register(Choice, ChoicesAdmin)
