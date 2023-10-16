from django.urls import path
from API.views import UserView, TokenView, ChatView

urlpatterns = [
    path('users/', UserView.as_view(), name='users'),
    path('token/', TokenView.as_view(), name='token'),
    path('chat/', ChatView.as_view(), name='chat')
]