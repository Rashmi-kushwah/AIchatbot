

from django.urls import path
from .views import chatbot_response,get_csrf_token,chatbot_page

urlpatterns = [
    path("chatbot-response/", chatbot_response, name="chatbot_response"),
    path("get-csrf-token/", get_csrf_token, name="get_csrf_token"),
    path("", chatbot_page, name="chatbot_page"),
]
