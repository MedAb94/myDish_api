from django.contrib import admin

# Register your models here.
from .models import Dish


class DishesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'is_available')
    list_display_links = ('id', 'name')
    list_filter = ('price',)
    list_editable = ('is_available',)
    search_fields = ('name', 'price')
    list_per_page = 25

admin.site.register(Dish, DishesAdmin)