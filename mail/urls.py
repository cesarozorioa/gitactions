from django.urls import path
from .views import EmailAPIView

urlpatterns = [      
    path('correo/',EmailAPIView.as_view(),name='correo')  
]