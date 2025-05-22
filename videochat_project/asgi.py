import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import videochat_project.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "videochat_project.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            videochat_project.routing.websocket_urlpatterns
        )
    ),
})
