from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.conf import settings

def send_websocket_data(todolist_id, json_data):
    room_name = f"{settings.MAIN_ROOM}_{todolist_id}"

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        room_name,
        {
            "type": "send_data",
            "data": json_data
        }
    )

