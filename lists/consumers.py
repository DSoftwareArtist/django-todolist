import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.conf import settings

class TodoListConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.todolist = self.scope['url_route']['kwargs']['todolist']
        self.room_group_name = '%s_%s' % (settings.MAIN_ROOM, self.todolist)

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    
    async def send_data(self, res):
        """ Receive message from room group """
        # Send data to WebSocket
        await self.send(text_data=json.dumps({
            "data": res,
        }))

