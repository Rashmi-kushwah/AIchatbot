import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chatbot.routing import websocket_urlpatterns  # Routing import karna zaroori hai

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbot_project.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)  # Yaha URLRouter add karo
    ),
})
