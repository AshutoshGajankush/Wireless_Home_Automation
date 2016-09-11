# Django views for REST services and home automation application - views.py

from myapp.models import Light
from rest_framework import viewsets
from django.shortcuts import render_to_response
from django.template import RequestContext
from myapp.serializers import LightSerializer
import requests
import json
"""
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
"""
class LightViewSet(viewsets.ModelViewSet):
    queryset = Light.objects.all()
    serializer_class = LightSerializer

def home(request):
    """
    roomstate = 'no'
    r = requests.get('http://127.0.0.1:8000/room/1/', auth=('pi', 'group5iot'))
    result = r.text
    output = json.loads(result)
    roomstate = output['name']
"""
    lightstate = 'OFF'
    r = requests.get('http://127.0.0.1:8000/light/1/', auth=('pi', 'group5iot'))
    result = r.text
    output = json.loads(result)
    lightstate = output['name']

    return render_to_response('myapp/index.html',
                             {'lightstate':lightstate},
                             context_instance=RequestContext(request))
