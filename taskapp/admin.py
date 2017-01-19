from django.contrib import admin
from models import *

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('created', 'last_modified', 'name', 'description', 'img_url', 'price')

admin.site.register(Item, ItemAdmin)