from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

from django.db import transaction as trans
from django.conf import settings

from django.contrib.auth.models import User
import logging
import json


logger = logging.getLogger(__name__)


class MainConsumer(WebsocketConsumer):

    def connect(self):
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        
        try:
            profile = User.objects.get(id=self.user_id)
            self.room_name = f"{settings.MAIN_ROOM}_{self.user_id}"
            with trans.atomic():
                profile.connected = True
                profile.save()

            async_to_sync(self.channel_layer.group_add)(
                self.room_name,
                self.channel_name
            )
            self.accept()
            print('connected boss')

        except User.DoesNotExist as exc:
            print('error boss')
            logger.info(f"USER {self.user_id} does not exist!")


    def disconnect(self, close_code):
        logger.info(f"USER {self.user_id} DISCONNECTED!")
        async_to_sync(self.channel_layer.group_discard)(
            self.room_name,
            self.channel_name
        )

    def send_data(self, event):
        data = event['data']

        logger.info('SENDING DATA\n')
        logger.info(event)

        # Send data to WebSocket (frontend)
        self.send(text_data=json.dumps({
            'data': data
        }))
