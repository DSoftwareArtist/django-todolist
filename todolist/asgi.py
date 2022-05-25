import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todolist.settings")
django_asgi_app = get_asgi_application()

# from channels.auth import AuthMiddlewareStack
from channels.sessions import SessionMiddlewareStack
# from channels.security.websocket import AllowedHostsOriginValidator
from channels.routing import ProtocolTypeRouter, URLRouter
import lists.routing


application = ProtocolTypeRouter({
  "http": django_asgi_app,
  "websocket": SessionMiddlewareStack(
        URLRouter(
          lists.routing.websocket_urlpatterns
        )
  )
})
