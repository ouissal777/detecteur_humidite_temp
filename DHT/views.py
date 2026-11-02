from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Dht11


@api_view(['GET'])
def latest(request):
    last = Dht11.objects.order_by('-id').first()
    return render(request, 'DHT/latest.html', {'last': last})
