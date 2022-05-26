from django.conf.urls import url
from lists.consumers import TodoListConsumer

websocket_urlpatterns = [
    url(r'^ws/todolist/(?P<todolist>\w+)/$', TodoListConsumer.as_asgi()),
]