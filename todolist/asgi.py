## todolist/asgi.py
import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import lists.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todolist.settings')

# application = get_asgi_application()
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            lists.routing.websocket_urlpatterns
        )
    ),
})