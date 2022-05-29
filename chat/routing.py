from django.urls import path
from chat import consumers

websocket_urlpatterns = [
    path('ws/<username>/', consumers.Chat.as_asgi()),
]