from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
class EmailAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        try:
            to_email = 'cesarozorioa@gmail.com'
            subject = 'Prueba de correo'
            message = 'Este es le mansaje o cuerpo'
            send_mail(subject, message, settings.EMAIL_HOST_USER,[to_email])
            return Response({'message':'Correo Enviado'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
