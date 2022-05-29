from django.urls import path
from chat import views

urlpatterns = [
    path('<str:username>/', views.chat, name='chat'),
]