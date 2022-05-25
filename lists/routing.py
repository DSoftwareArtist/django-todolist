from django.urls import re_path

from lists.consumers import *


websocket_urlpatterns = [
    re_path(r'ws/(?P<user_id>((\w+|-+)+))/$', MainConsumer.as_asgi()),
]
