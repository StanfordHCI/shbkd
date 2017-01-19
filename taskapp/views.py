from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import viewsets

# Create your views here.
from models import *
from serializers import *

class ItemViewSet(viewsets.ModelViewSet):
    '''
    * Model Description: Item is the model for the items in the shopping app.
    * CRUD on Item model
    * C - CREATE - POST /item/ - allowed for anyone
    * R - READ - GET /item/ (list) - allowed for anyone
    * R - READ - GET /item/[id]/ (detail) - allowed for anyone
    * U - UPDATE - PATCH /item/[id]/ - allowed for anyone
    * D - DELETE - DELETE /item/[id]/ - allowed for anyone
    '''
    queryset = Item.objects.all()
    permission_classes = (AllowAny,)
    filter_fields = '__all__'
    serializer_class = ItemSerializer