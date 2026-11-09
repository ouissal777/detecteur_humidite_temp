from .models import Dht11
from .serializers import DHT11serialize
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
import telebot

@api_view(["GET"])
def Dlist(request):
    all_data = Dht11.objects.all()
    data = DHT11serialize(all_data, many=True).data
    return Response({"data": data})

class Dhtviews(generics.CreateAPIView):
    queryset = Dht11.objects.all()
    serializer_class = DHT11serialize

class Dhtviews(generics.CreateAPIView):
    queryset = Dht11.objects.all()
    serializer_class = DHT11serialize

    def perform_create(self, serializer):
        data = serializer.save()
        temperature = data.temp

        if temperature > 25:
            message = f"Alerte ! Temperature = {temperature} °C"

            send_mail(
                subject="Alerte Temperature",
                message=message,
                from_email=settings.EMAIL_SENDER,
                recipient_list=[settings.DESTINATAIRE],
                fail_silently=False
            )
 
            bot = telebot.TeleBot(settings.TELEGRAM_TOKEN)
            bot.send_message(settings.TELEGRAM_CHAT_ID, message)